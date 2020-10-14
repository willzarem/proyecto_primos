# borrowed and modified from https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file/18625294
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from findpeaks import findpeaks
from scipy.signal import find_peaks

spf = wave.open("clapping1.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))



A = signal
peaks, _ = find_peaks(A, distance=10000)
print(peaks)
# This prints the desired indices [10 45]



final_peaks = []
for peak in peaks:
    if A[peak] > 2000:
        print("clap", peak, A[peak])
plt.plot(A)
plt.plot(peaks, A[peaks], "x")
plt.show()
# print(signal)

# print("type is ", type(signal))
# print(len(signal))
# listed = signal.tolist()
# print(max(listed), min(listed))
# for l in listed:
#     if l > 2000 or l < -2000:
#         print("clap")

#fp = findpeaks(method='topology', interpolate= 10)
#results= fp.fit(signal)
#print(len(results), results)
#fp.plot()
#X = list(signal)
#print(X)
#Xi = findpeaks.interpolate_line1d(X, method='linear', n=10, showfig=True)
#print('Input data lenth: %s, interpolated length: %s' %(len(signal), len(Xi)))

#plt.figure(1)
#plt.title("Signal Wave...")
#plt.plot(Time, signal)
# #plt.show()
# mu, sigma = 0, 0.1 # mean and standard deviation
# s = signal #np.random.normal(mu, sigma, 1000)
# abs(mu - np.mean(s))
# abs(sigma - np.std(s, ddof=1))
# count, bins, ignored = plt.hist(s, 30, density=True)

# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.show()