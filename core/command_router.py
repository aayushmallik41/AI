from core.speaker import speak
from core.system_controller import (
    open_chrome,
    open_notepad,
    system_status,
    shutdown_system
)

def route_command(command: str):
    if command == "":
        return None

    if "exit" in command or "quit" in command:
        speak("Goodbye Boss.")
        return "EXIT"

    if "open chrome" in command:
        open_chrome()
        return None

    if "open notepad" in command:
        open_notepad()
        return None

    if "system status" in command:
        system_status()
        return None

    if "shutdown" in command:
        speak("Please confirm shutdown by saying yes")
        return "CONFIRM_SHUTDOWN"

    speak("Command not recognized.")
    return None
