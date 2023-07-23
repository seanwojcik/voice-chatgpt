import sys
from speech_to_text import record_audio, transcribe_audio
from text_to_speech import text_to_speech
from chatgpt_api import chat_gpt


def main(api_key, system_description, voice="Samantha"):
    messages = []
    if system_description is None:
        system_description = "You are helpful AI bot. Only speak one or two sentences at a time. Be friendly, accurate, and helpful. Ask questions to keep the conversation going."

    while True:
        # Record user input
        record_audio("input.wav")
        user_message = transcribe_audio("input.wav", api_key)
        if not user_message:
            print("Sorry, I couldn't understand what you said. Please try again.")
            continue
        print(f"You: {user_message}")

        # Add user message to ChatGPT messages dict
        messages.append({"role": "system", "content": system_description})
        messages.append({"role": "user", "content": user_message})

        # Get the ChatGPT response
        response_text = chat_gpt(messages, api_key)
        print(f"\nAssistant: {response_text}")
        messages.append({"role": "assistant", "content": response_text})

        # Convert response text to speech and say it
        text_to_speech(response_text, voice)


if __name__ == "__main__":
    """
    Usage: python main.py OPENAI_API_KEY -sd [SYSTEM-DESCRIPTION] -v [VOICE]
    """
    if len(sys.argv) < 1:
        print(
            "Usage: python main.py OPENAI_API_KEY -sd [SYSTEM-DESCRIPTION] -v [VOICE]"
        )
        exit(1)

    # Define api key, system description, and voice variables
    api_key = sys.argv[1]
    sys_desc = sys.argv[sys.argv.index("-sd") + 1] if "-sd" in sys.argv else None
    voice = sys.argv[sys.argv.index("-v") + 1] if "-v" in sys.argv else "Samantha"

    print(
        "\nWhen it is your turn to talk, press Enter to stop recording each message, or press ESC to quit.]"
    )

    main(api_key, sys_desc, voice)
