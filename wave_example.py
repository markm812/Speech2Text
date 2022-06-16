import wave
import numpy as np
import matplotlib.pyplot as plt
# Audio signal
# - number of channels
# - sample width
# - framerate
# - number of frames
# - value of a frame
def printSampleInfo(wav):
    print("Number of  channel: ", wav.getnchannels())
    print("Sample width: ", wav.getsampwidth())
    print("Framerate: ", wav.getframerate())
    print("Number of frames: ", wav.getnframes())
    print("Pararmeters: ", wav.getparams())
    print(f'The audio is {wav.getnframes()/wav.getframerate()} seconds long.')

# Sample info
obj = wave.open("./data/speech.wav","rb")
printSampleInfo(obj)

# Sample parameters
sample_frequency = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)
t_audio = n_sample / sample_frequency

obj.close()

# .wav to array notation
signal_array = np.frombuffer(signal_wave,dtype = np.int16)
times = np.linspace(0,t_audio, num = n_sample)

# Plot
plt.figure(figsize=(15,3))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()