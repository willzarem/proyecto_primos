# borrowed and modified from https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file/18625294

import numpy as np
import wave
import sys


spf = wave.open("clapping1.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))

print(signal)

print("type is ", type(signal))
print(len(signal))
listed = signal.tolist()
print(max(listed), min(listed))
for l in listed:
    if l > 2000 or l < -2000:
        print("clap")
