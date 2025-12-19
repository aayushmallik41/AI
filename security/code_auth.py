from core.speaker import speak

# Temporary hardcoded codes (will be secured later)
OWNER_CODE = "1234"
GUEST_CODE = "0000"

def verify_code(code: str):
    """
    Returns role: owner / guest / None
    """
    if code == OWNER_CODE:
        speak("Owner verified.")
        return "owner"

    if code == GUEST_CODE:
        speak("Guest access granted. Security mode active.")
        return "guest"

    speak("Invalid security code.")
    return None
