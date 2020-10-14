import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.signal import find_peaks

class Clap:
    def __init__(self):
        filename = sys.argv[1]
        spf = wave.open(filename, "r")
        signal = spf.readframes(-1)
        self.signal = np.fromstring(signal, "Int16")
        self.fs = spf.getframerate()
        self.peaks = np.array([])
        self.final_peaks = []
    
    def detectClap(self):

        Time = np.linspace(0, len(self.signal) / self.fs, num=len(self.signal))

        PEAK_DELTA = max(self.signal)/2
        A = self.signal
        peaks, _ = find_peaks(A, distance=PEAK_DELTA)
        self.peaks = peaks;   
        #print(peaks)

        mean = np.mean(A, axis=0)
        sd = np.std(A, axis=0)

        final_peaks = []
        for peak in peaks:
            if A[peak] > (mean + 6*sd):
                final_peaks.append(peak)
                print("clap", peak, A[peak])
        self.final_peaks = final_peaks        
        return final_peaks

    def printPeaks(self):
        A = self.signal
        plt.plot(A)
        plt.plot(self.peaks, A[self.peaks], "x")
        plt.show()

clap = Clap()
print(clap.detectClap())
clap.printPeaks()
