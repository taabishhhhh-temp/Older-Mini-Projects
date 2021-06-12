#! /usr/bin/python3

import time
import pyttsx3
print()
print("********************")
print("*****STOP WATCH*****")
print("********************")
print()

speaker = pyttsx3.init()

def speak(timeleft):
    speaker.say(timeleft)
    speaker.runAndWait()

speak("enter number of seconds")
timeleft = int(input("ENTER NO OF SECONDS\n"))
while timeleft >= 0:
    if timeleft == 0:
        print("TIME\'S UP")
        speak("times up")
        break
    else:
        print(timeleft, "SECONDS REMAINING")
        speak(timeleft)
        time.sleep(1)
        timeleft -= 1
print()
