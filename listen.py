import sounddevice as sd
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")   # load once

SAMPLE_RATE = 16000
SECONDS = 5

#Record the audio
print("Speak now please.")
audio = sd.rec(int(SECONDS * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = 1, dtype = 'float32')

sd.wait()

#Turn the audio into a 1D array
audio = audio.flatten()


segments, info = model.transcribe(audio, language="en") 

sentence = ""

#Put the audio array into a string
for segment in segments:
    sentence += segment.text.strip()
    sentence += " "

#Remove the extra space
sentence = sentence.strip()

if(sentence == ""):
    print("Nothing recorded")
else:
    print(f"{sentence}")





