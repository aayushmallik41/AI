from core.listener import listen
from core.speaker import speak
from core.command_router import route_command
from core.system_controller import shutdown_system
from config.settings import OWNER_NAME, ASSISTANT_NAME

from security.code_auth import verify_code
from security.audit_log import log_event


def main():
    speak(f"Hello {OWNER_NAME}, {ASSISTANT_NAME} is online.")

    security_mode = False
    user_role = None
    pending_action = None

    while True:
        heard_text = listen()

        if not heard_text:
            continue

        if ASSISTANT_NAME.lower() not in heard_text:
            continue

        command = heard_text.replace(ASSISTANT_NAME.lower(), "").strip()
        print(f"COMMAND: {command}")

        # ---------------- SECURITY MODE ACTIVATION ----------------
        if "activate security mode" in command:
            security_mode = True
            user_role = None
            speak("Security mode activated. Please provide security code.")
            log_event("Security mode activated")
            continue

        # ---------------- SECURITY VERIFICATION ----------------
        if security_mode and user_role is None:
            role = verify_code(command)
            if role:
                user_role = role
                log_event(f"{role} verified")
            continue

        # ---------------- OWNER DISABLE SECURITY ----------------
        if user_role == "owner" and "deactivate security mode" in command:
            security_mode = False
            user_role = None
            speak("Security mode deactivated.")
            log_event("Security mode deactivated by owner")
            continue

        # ---------------- GUEST RESTRICTIONS ----------------
        if user_role == "guest" and "shutdown" in command:
            speak("Shutdown is not allowed for guest users.")
            log_event("Guest attempted restricted shutdown")
            continue

        # ---------------- SHUTDOWN CONFIRMATION ----------------
        if pending_action == "SHUTDOWN_CONFIRM":
            if "yes" in command:
                shutdown_system()
                log_event("System shutdown confirmed")
                pending_action = None
                continue
            else:
                speak("Shutdown cancelled.")
                pending_action = None
                continue

        # ---------------- COMMAND ROUTING ----------------
        result = route_command(command)

        if result == "EXIT":
            break

        if result == "CONFIRM_SHUTDOWN":
            pending_action = "SHUTDOWN_CONFIRM"


if __name__ == "__main__":
    main()
