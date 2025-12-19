import os
import psutil
from core.speaker import speak

def open_chrome():
    speak("Opening Chrome")
    os.system("start chrome")

def open_notepad():
    speak("Opening Notepad")
    os.system("start notepad")

def system_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    speak(f"CPU usage is {cpu} percent and RAM usage is {ram} percent")

def shutdown_system():
    speak("Shutting down the system in 10 seconds")
    os.system("shutdown /s /t 10")
