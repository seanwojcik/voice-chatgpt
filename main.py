# main.py

import os
import sys
from speech_to_text import record_audio, transcribe_audio
from text_to_speech import text_to_speech, play_audio
from chatgpt_api import chat_gpt, extract_message


def main(api_key, system_description):
    messages = []
    if system_description is None:
        system_description = "You are helpful AI bot. Only speak one or two sentences at a time. Be friendly, accurate, and helpful. Ask questions to keep the conversation going."

    while True:
        # Record user input
        print("Please speak your message:")
        record_audio("input.wav")
        user_message = transcribe_audio("input.wav", api_key)

        if not user_message:
            print("Sorry, I couldn't understand what you said. Please try again.")
            continue

        print(f"You: {user_message}")
        messages.append({"role": "system", "content": system_description})
        messages.append({"role": "user", "content": user_message})

        # Get the ChatGPT response
        response_text = chat_gpt(messages, api_key)
        print(f"Assistant: {response_text}")
        messages.append({"role": "assistant", "content": response_text})

        # Convert response text to speech and play it
        text_to_speech(response_text, "response.mp3")
        play_audio("response.mp3")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py OPENAI_API_KEY [SYSTEM-DESCRIPTION]")
        exit(1)

    api_key = sys.argv[1]
    main(api_key, sys.argv[2] if len(sys.argv) > 2 else None)
