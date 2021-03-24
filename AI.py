import pyttsx3
import datetime
import speech_recognition 
import wikipedia
import os
import webbrowser   
import sys

import subprocess
from playsound import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def chat():
        speak("You are now in chat mode")
        ci=0
        while ci<2:
                if ci==1:
                        speak("Ending the Chat")
                        sys.exit(0)
                else:
                        r = speech_recognition.Recognizer()
                        with speech_recognition.Microphone() as source:
                                
                                
                                r.adjust_for_ambient_noise(source) 
                                print("Say Something")
                                speak("Say Something")
                                r.energy_threshold += 1780
                                
                                audio = r.listen(source,timeout=1,phrase_time_limit=2)
                                try:
                                        s=r.recognize_google(audio,language='en-in').lower()
                                        print('I think you spoke:\n'+s)
                                        speak("you said"+s)   

                                        #-----------------------
                                        # Logic : Logic: Logic
                                        # of chating Simple but Smart
                                        #----------------------- 
                                        if 'your name' in s:
                                                print("My name is Harvis sir")
                                                speak("My name is Harvis sir")
                                        elif 'your creator' in s:
                                                print("My Creator is Harsh ")
                                                speak("My Creator is Master Harsh")
                                        elif 'tired' in s:
                                                print("No sir I can never be tired and You cannot also because a  Human made me")
                                                speak("No sir I can never be tired and You cannot also because a  Human made me")

                                                
                                        elif 'chat' in s:
                                                
                                                speak("Thanks sir..")
                                        elif 'f*** off ' in s:
                                                speak("Then give me your ass")
                                                ci=1
                                        elif 'your work' in s:
                                                speak("my work is to assist you like a friend")
                                        elif 'your speciality' in s:
                                                speak("According to my codes,I can do some human activities")
                                        elif 'your desire' in s:
                                                  speak("to update myself according to highest artificial robot")
                                        elif 'hello' in s:
                                                speak("Hi there buddy")
                                       
                                        elif 'cancel' in s:
                                                ci=1

                                       
                                        elif 'marry you' in s:
                                                speak("It is not possible..I am only a robot")
                                       
                                        elif 'kill you' in s:
                                                speak("why what is my mistake")
                                               
                                                
                
                
                
                
 
                
                                        else:
                                                print("")

                
                                except:
                                        print("")



   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
def c():
        sys.exit(0)
def tc():
        i=0
        while i<4:
                if(i==2):
                        speak("Thanks sir, I am aborting the AI commands...")
                        c()
                elif(i==3):
                        
                        return i
                elif(i==1):
                        return i
                else:
                        r = speech_recognition.Recognizer()
                        with speech_recognition.Microphone() as source:
                                r.adjust_for_ambient_noise(source) 
                                print("Say Something")
                                speak("Say Something")
                                r.energy_threshold += 1780
                                
                                audio = r.listen(source,timeout=3,phrase_time_limit=2)
                                try:
                                        s=r.recognize_google(audio,language='en-in').lower()
                                        print('I think you said:\n'+s)
                                        speak("you said"+s)
                                        if 'wikipedia' in s:
                                                speak("I am searching wikipedia")
                                                s = s.replace("wikipedia","")
                                                speak("According to Wikipedia")
                                                print(wikipedia.summary(s,sentences=2))
                                                speak(wikipedia.summary(s,sentences=2))
                                        elif 'youtube' in s:
                                                speak("I am searching youtube")
                                                speak("success. I have found this..")
                                                s = s.replace("search youtube","")
                                                webbrowser.open('https://www.youtube.com/results?search_query='+s)
                                        elif 'open youtube' in s:
                                                speak("Opening Youtube in chrome...Please wait")
                                                webbrowser.open('http://youtube.com')
                                        elif 'google' in s:
                                                speak("Opening Google in Chrome ...Please wait")
                                                webbrowser.open('http://google.com')
                                        elif  'facebook' in s:
                                                speak("Opening Facebook ...Please wait")
                                                webbrowser.open('http://facebook.com')
                                        elif 'gmail' in s:
                                                speak("Opening Gmail...Please wait")
                                                webbrowser.open('http://gmail.com')
                                        elif'song' in s:
                                                speak("Sure sir.")
                                                playsound("C:\\Users\\username\\Desktop\\folder\Imagine Dragons  Believer.mp3")
                                       
                                        elif 'control panel' in s:
                                                subprocess.Popen(["Control.exe"])
                                       
                                        elif 'wordpad' in s:
                                                subprocess.Popen(["wordpad.exe"])
                                        
                                  
                                        elif 'shutdown pc'  in s:
                                                os.system("shutdown /s /t 15")
                                        elif 'cancel shutdown' in s:
                                                os.system('abort/a') 
                                        
                                        
                                        elif 'cancel' in s:
                                                i=2
                                        elif 'chat' in s:
                                                i=1
                                                chat()
                                        else:
                                                print("") 
                                except:
                                        print("")
        
    
           
        
       

        
       
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")
        

                     
if __name__ == "__main__":
   
    wish()
    speak("Hi there I am Harvis... I am an AI robot..")
    
    tc()
   
    
       
            
       
    
    