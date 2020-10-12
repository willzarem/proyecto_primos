
import pyaudio
import wave
import sys

CHUNK = 1024

output = "./assets/piano2.wav"
output = "./output/1.wav"
wf = wave.open(output, 'rb')

p = pyaudio.PyAudio()

print("channels %s", wf.getnchannels())

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()