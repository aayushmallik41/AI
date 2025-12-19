from core.listener import listen
from core.speaker import speak
from config.settings import OWNER_NAME

def main():
    speak(f"Hello {OWNER_NAME}, Jarvis is online.")

    while True:
        command = listen()

        if not command:
            continue

        if "exit" in command or "quit" in command:
            speak("Goodbye Boss.")
            break

        speak("I heard you.")

if __name__ == "__main__":
    main()
