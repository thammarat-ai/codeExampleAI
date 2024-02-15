# Example 11.14

import soundfile as sf
import matplotlib.pyplot as plt

path = 'test.wav'
data, rate = sf.read(path)
# Plot the signal read from wav file
plt.subplot(211)
plt.title('Spectrogram of a wav file')
plt.plot(data[:,0])
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.specgram(data[:,0],Fs=rate)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
