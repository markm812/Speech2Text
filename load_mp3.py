from pydub import AudioSegment
audio = AudioSegment.from_wav("./data/speech.wav")

audio = audio + 6
audio = audio + 2
audio = audio.fade_in(2000) 

audio.export("./data/mashup.mp3",format="mp3")
audio2 = AudioSegment.from_mp3("./data/mashup.mp3")
print("Done.")
