# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:40:23 2025

@author: Karthik
"""

import speech_recognization as sr
recognizer = sr.Recognizer() #begin of the program 

with sr.Microphone() as source:
    print("Hey! Say Something....")
    recognizer.adjust_for_ambient_noise(source) #remove the noise
    audio = recognizer.listen(source) #listen the audio from the source
   
    #pass the audio to GenAI model
    
try :
    print("You said" + recognizer.recognize.google(audio))
except sr.UnknownvalueError :
    print("Google speech recongnization could not understand audio")
except sr.RequestError as e :
    print("couldnot request results; {0}".format(e))
    
