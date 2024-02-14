# Example 11.13
# pip install sounddevice soundfile

import sounddevice as sd
import soundfile as sf
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy import signal

fs=44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
print ("Recording ...")
sd.wait()
print ("Playing Audio ...")
sd.play(myrecording, fs)
sd.wait()
print ("Writing Audio: test.wav")
filename = "test.wav"
sf.write(filename, myrecording, fs)

# plot wave by audio frames
plt.figure(figsize=(10, 5))
plt.subplot(2,1,1)
plt.plot(myrecording[:,0], 'r-', label='Left');
plt.legend()
plt.subplot(2,1,2)
plt.plot(myrecording[:,1], 'g-', label='Right');
plt.legend()
plt.show()
