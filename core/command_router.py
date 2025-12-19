from core.speaker import speak

def route_command(command: str):
    """
    Routes the command to the appropriate action.
    Day-2: only basic commands.
    """

    if "exit" in command or "quit" in command:
        speak("Goodbye Boss.")
        return "EXIT"

    if command.strip() == "":
        return None

    speak("Command received.")
    return None
