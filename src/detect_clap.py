import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.signal import find_peaks

filename = sys.argv[1]
spf = wave.open(filename, "r")

signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))


PEAK_DELTA = max(signal)/2
A = signal
peaks, _ = find_peaks(A, distance=PEAK_DELTA)

print(peaks)

mean = np.mean(A, axis=0)
sd = np.std(A, axis=0)

final_peaks = []
for peak in peaks:
    if A[peak] > (mean + 6*sd):
        final_peaks.append(peak)
        print("clap", peak, A[peak])
plt.plot(A)
plt.plot(peaks, A[peaks], "x")
plt.show()