import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

import numpy as np
import wave
import sys

spf = wave.open("clapping1.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

peaks, _ = find_peaks(signal, height=0)

print(len(peaks), len(signal))
n = 5

indices = (-peaks).argsort()[:n]

print(indices)
#for p in peaks:
#    print("peak")

def peak_detect(data):
    max_val = np.amax(abs(data)) 
    peak_ndx = np.where(data==max_val)
    if len(peak_ndx[0]) == 0: #if nothing found then the max must be negative
        peak_ndx = numpy.where(data==-max_val)
    return peak_ndx

peaks = peak_detect(signal)
for p in peaks:
    print(p, "clap")
#plt.plot(signal)
#plt.plot(peaks, signal[peaks], "x")
#plt.plot(np.zeros_like(signal), "--", color="gray")
#plt.show()
