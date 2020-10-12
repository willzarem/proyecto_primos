import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.signal import find_peaks

spf = wave.open("clapping2.wav", "r")

signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))


PEAK_DELTA = 10000
A = signal
peaks, _ = find_peaks(A, distance=PEAK_DELTA)

print(peaks)

final_peaks = []
for peak in peaks:
    if A[peak] > 3000:
        final_peaks.append(peak)
        print("clap", peak, A[peak])
plt.plot(A)
plt.plot(peaks, A[peaks], "x")
plt.show()