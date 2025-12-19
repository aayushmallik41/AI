from core.listener import listen
from core.speaker import speak
from core.command_router import route_command
from config.settings import OWNER_NAME, ASSISTANT_NAME

def main():
    speak(f"Hello {OWNER_NAME}, {ASSISTANT_NAME} is online.")

    while True:
        heard_text = listen()

        if not heard_text:
            continue

        # Wake word check
        if ASSISTANT_NAME.lower() not in heard_text:
            print("Wake word not detected.")
            continue

        # Extract command after wake word
        command = heard_text.replace(ASSISTANT_NAME.lower(), "").strip()
        print(f"COMMAND AFTER WAKE WORD: {command}")

        result = route_command(command)

        if result == "EXIT":
            break

if __name__ == "__main__":
    main()
