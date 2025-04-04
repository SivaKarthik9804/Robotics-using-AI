
@author: Karthik
"""

import speech_recognition as sr
import pyttsx3
import datetime as dt
import requests
import os
import pygame 
import serial

# Initialize modules
pygame.mixer.init()
listener = sr.Recognizer()
speaker = pyttsx3.init()

# Set Speech Properties
speaker.setProperty('rate', 130)
voices = speaker.getProperty('voices')  # Fixed typo
speaker.setProperty('voice', voices[1].id)  # Female voice

# Virtual Assistant Name
va_name = 'cmos'

# Set the COM port (adjust as per your device)
try:
    arduino = serial.Serial('COM7', 9600)  # Adjust COM port as needed
except serial.SerialException:
    print("Error: Arduino not connected.")

# Function to speak
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

# Function to take voice command
def take_command(idle_mode=True):
    command = ''
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)  # Reduces background noise
            
            if idle_mode:
                print('Waiting for wake-up word...')
                voice = listener.listen(source, timeout=2)
            else:
                print("Listening...")
                voice = listener.listen(source)
                
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        return ''  # Speech not recognized
    except sr.RequestError:
        return ''  # API not reachable
    except Exception as e:
        print(f'An error occurred: {e}')
        return ''

# Function to listen for wake-up word
def listen_for_wakeup_word():
    while True:
        idle_command = take_command(idle_mode=True)
        if va_name in idle_command:
            print('Waking up...')
            speak(f'I am your {va_name}, How can I help you?')
            main()

# Main Function
def main():
    while True:
        user_command = take_command(idle_mode=False)  
        if user_command:
            print(f"User command received: {user_command}")  # Fixed typo

            if 'stop' in user_command:
                speak('Going idle. Please call me with my name.')
                listen_for_wakeup_word()

            elif 'on led' in user_command:
                print("TURNING ON LED")
                if arduino.is_open:
                    arduino.write(b'1')  # Corrected byte writing
                    speak('Turning ON LED')
                else:
                    speak('Error: Arduino not connected.')

            elif 'off led' in user_command:
                print("TURNING OFF LED")
                if arduino.is_open:
                    arduino.write(b'0')
                    speak('Turning OFF LED')
                else:
                    speak('Error: Arduino not connected.')

            else:
                speak("Sorry, I didn't understand the command.")

# Run the assistant
if __name__ == "__main__":
    speak(f"My name is {va_name}.")
    listen_for_wakeup_word()
