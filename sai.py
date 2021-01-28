import speech_recognition as sr
import pyttsx3
import vlc
from mutagen.id3 import ID3
import os
# from pygame import mixer  # Load the popular external library
import webbrowser



# from playmusic import directorychooser 

#Sai_variables
sai_ear = sr.Recognizer()
sai_mouth = pyttsx3.init()
sai_brain = ""
voices = sai_mouth.getProperty('voices') 
url = 'http://docs.python.org/'
# New Voice ID
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
jp_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0" 
kr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
# Set New Voice
sai_mouth.setProperty('voice', kr_voice_id)
# Talk function 
def talk(brain):
    print("Sai: " + brain)
    sai_mouth.say(brain)
    sai_mouth.runAndWait() 

# Start Application
# Sai say Hello 
sai_mouth.say("안녕, 제이크")
sai_mouth.runAndWait() 
# Start the loop
# while True:
    
    
    #with so Mic turn off when we are done
with sr.Microphone() as mic:
    print("Sai: I'm Listening")
    text = sai_ear.listen(mic)
    print("Sai: ...")
    try:
        recognised_text = sai_ear.recognize_google(text)
        print("You: " + recognised_text)
        
    except sr.UnknownValueError:
        print("You: ?")
    except sr.RequestError as e:
        print("")

    ############################################################################################
    #Sai reaction 
    if recognised_text == "":
        sai_brain = "I can't hear you"
        talk(sai_brain)
    elif recognised_text == "hello":
        sai_brain = "Hello Jake"
        talk(sai_brain)
    elif recognised_text == "today":
        sai_brain ="thu 6"
        talk(sai_brain)
    elif recognised_text == "play":
        sai_brain ="What song world you like to play"
        talk(sai_brain)
        webbrowser.open(r"C:\Users\Jake\Music\(SNKK) TuNombreTSO\(SNKK) Kimi no Na wa Original Soundtrack [Your Name]\02 - Mitsuba no Tsuugaku.mp3")
    elif "bye" in recognised_text:
        sai_brain = "Bye"
        talk(sai_brain)
        # break
    elif recognised_text == "open":
        sai_brain ="Opening"
        talk(sai_brain)
        webbrowser.open("youtube.com")
    else:
        sai_brain = "I'm fine thank you and you"
        talk(sai_brain)
        # break
        #############################################################################################


