import speech_recognition as sr

sai_ear = sr.Recognizer()

#with so Mic turn off when we are done
with sr.Microphone() as source:
    print("Sai: I'm Listening")
    text = sai_ear.listen(source)


    try:
        recognised_text = sai_ear.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")