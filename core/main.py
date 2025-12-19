from core.listener import listen
from core.speaker import speak
from core.command_router import route_command
from config.settings import OWNER_NAME, ASSISTANT_NAME

def main():
    speak(f"Hello {OWNER_NAME}, {ASSISTANT_NAME} is online.")
pending_action = None

while True:
        heard_text = listen()

        if not heard_text:
            continue

        if ASSISTANT_NAME.lower() not in heard_text:
            continue

        command = heard_text.replace(ASSISTANT_NAME.lower(), "").strip()
        print(f"COMMAND: {command}")

        if pending_action == "SHUTDOWN_CONFIRM":
            if "yes" in command:
                from core.system_controller import shutdown_system
                shutdown_system()
                pending_action = None
                continue
            else:
                speak("Shutdown cancelled.")
                pending_action = None
                continue

        result = route_command(command)

        if result == "EXIT":
            break

        if result == "CONFIRM_SHUTDOWN":
            pending_action = "SHUTDOWN_CONFIRM"