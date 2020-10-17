from multiprocessing import Process, Queue
import time
import pyaudio
import numpy as np
import aubio



# def sendSoundData(child_conn):
#     child_conn.send("hello world")
#     child_conn.close()

p = pyaudio.PyAudio()

output = "./output/1.wav"

buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format, channels=n_channels, rate=samplerate, input=True, frames_per_buffer=buffer_size)

record_duration = 0
total_frames = 0

tolerance = 0.8
win_s = 4096
hop_s = buffer_size
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

def record(child_conn):
    print("*** starting recording")
    while True:
        #print("In True")
        try:
            #print("about to read audio buffer")
            audiobuffer = stream.read(0)
            #print("about to get signal")
            signal = np.frombuffer(audiobuffer, dtype=np.float32)
            
            #print("about to send signal")
            child_conn.send("sending signal")
            #print("in record")
        except KeyboardInterrupt:
            print("*** Stopped")
            break
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    print("*** done recording")
    stream.stop_stream()
    stream.close()
    child_conn.close()

def test(child_conn):
    child_conn.send("hello")
    child_conn.close()