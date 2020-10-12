import pyaudio
import wave
import sys


CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()

'''-------------------------------------------------------------
The above was taken from https://people.csail.mit.edu/hubert/pyaudio/docs/ and simply
plays a .wav file that is passed in. The following was adapted from https://realpython.com/playing-and-recording-sound-python/#pyaudio_1 to record user input and replay it.
'''


SAMPLE_SIZE = 1024
sample_format = pyaudio.paInt32
channels = 1

fs = 44100
seconds = 10
filename = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=sample_format, channels = channels, rate = fs, frames_per_buffer = SAMPLE_SIZE, input=True)

frames = []

for i in range(0, int(fs/SAMPLE_SIZE * seconds)):
    data = stream.read(SAMPLE_SIZE)
    frames.append(data)

stream.stop_stream()
stream.close()

p.terminate()

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
