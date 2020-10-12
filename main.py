import pyaudio
import wave
import sys
import numpy as np
import aubio

p = pyaudio.PyAudio()

output = "./output/1.wav"

buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format, channels=n_channels, rate=samplerate, input=True, frames_per_buffer=buffer_size)

record_duration = 5
outputsink = aubio.sink(output, samplerate)
total_frames = 0

tolerance = 0.8
win_s = 4096
hop_s = buffer_size
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

print("*** starting recording")
while True:
    try:
        audiobuffer = stream.read(buffer_size)
        signal = np.frombuffer(audiobuffer, dtype=np.float32)

        pitch = pitch_o(signal)[0]
        confidence = pitch_o.get_confidence()
        if pitch > 50:
            print("signal")
            print("{} / {}".format(pitch, confidence))

        if outputsink:
            outputsink(signal, len(signal))

        if record_duration:
            total_frames += len(signal)
            if record_duration * samplerate < total_frames:
                break
    except KeyboardInterrupt:
        print("*** Stopped")
        break

print("*** done recording")
stream.stop_stream()
stream.close()

wf = wave.open(output, 'rb')

print("channels %s", wf.getnchannels())

read_stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=wf.getframerate(),
                     output=True)

data = wf.readframes(buffer_size)
print('playing')
while data != '':
    read_stream.write(data)
    data = wf.readframes(buffer_size)

read_stream.stop_stream()
read_stream.close()
p.terminate()
