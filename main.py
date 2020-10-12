import pyaudio
import sys
import numpy as np
import aubio

p = pyaudio.PyAudio()

buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels =