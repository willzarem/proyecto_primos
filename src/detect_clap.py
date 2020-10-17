import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.signal import find_peaks
import sys
sys.path.append('/Users/diher/git/proyecto_primos/sound_samples')

class Clap:
    def __init__(self, file):
        if(file == 'continuous'):
            self.signal = os.p
        else:
            filename = file
            spf = wave.open(filename, "r")
            signal = spf.readframes(-1)
            self.signal = np.fromstring(signal, "Int16")
            self.fs = spf.getframerate()
        self.peaks = []
        self.final_peaks = []
    
    def detectClap(self):

        Time = np.linspace(0, len(self.signal) / self.fs, num=len(self.signal))

        PEAK_DELTA = max(self.signal)/2
        A = self.signal
        peaks, _ = find_peaks(A, distance=PEAK_DELTA)
        self.peaks = peaks;   

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

clap = Clap(sys.argv[1])
print(clap.detectClap())
clap.printPeaks()
