import speech_recognition as sr

filename = 'audio/male.wav'

r = sr.Recognizer()

with sr.AudioFile(filename) as audio:
    audio_data = r.record(audio)
    print(audio_data)
    text = r.recognize_google(audio_data)
    print(text)