import os
import subprocess

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def text_to_speech(text, voice="Samantha"):
    """
    Uses the "say" command on macOS to convert text to speech and say it.
    """
    try:
        subprocess.run(["say", text, "-v", voice])
    except FileNotFoundError:
        print("The 'say' command is not found. Make sure you are on macOS.")
    except Exception as e:
        print(f"An error occurred: {e}")
