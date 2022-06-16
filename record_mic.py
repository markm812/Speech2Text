import wave
import pyaudio

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAMERATE = 8000

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, 
    channels=CHANNELS,
    rate = FRAMERATE,
    input = True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Start recording...")
second = 5
frames = []
for i in range(0,int(FRAMERATE/FRAMES_PER_BUFFER*second)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav","wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(FRAMERATE)
obj.writeframes(b"".join(frames))
obj.close()