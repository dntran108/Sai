import speech_recognition as sr
import pyttsx3

#Sai_variables
sai_ear = sr.Recognizer()
sai_mouth = pyttsx3.init()
sai_brain = ""
voices = sai_mouth.getProperty('voices') 
# New Voice ID
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
jp_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0" 
kr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0"
# Set New Voice
sai_mouth.setProperty('voice', kr_voice_id)


# Start Application
# Sai say Hello 
sai_mouth.say("안녕, 제이크")
sai_mouth.runAndWait() 
#with so Mic turn off when we are done
with sr.Microphone() as mic:
    print("Sai: I'm Listening")
    text = sai_ear.listen(mic)
    print("Sai: ...")
try:
    recognised_text = sai_ear.recognize_google(text)
    print("You: " + recognised_text)
except sr.UnknownValueError:
    print("")
except sr.RequestError as e:
    print("")




############################################################################################
 
if recognised_text == "":
    sai_brain = "I can't hear you"
elif recognised_text == "hello":
    sai_brain = "Hello Jake"
elif recognised_text == "today":
    sai_brain ="thu 6"
else:
    sai_brain = "I'm fine thank you and you"


#############################################################################################


  
# for voice in voices: 
#     # to get the info. about various voices in our PC  
#     print("Voice:") 
#     print("ID: %s" %voice.id) 
#     print("Name: %s" %voice.name) 
#     print("Age: %s" %voice.age) 
#     print("Gender: %s" %voice.gender) 
#     print("Languages Known: %s" %voice.languages) 

sai_mouth.say(sai_brain)
sai_mouth.runAndWait() 
