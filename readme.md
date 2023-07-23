# Voice ChatGPT

This app allows a voice chat conversation with OpenAI's ChatGPT. The user's voice messages are received via the microphone, and GPT's chat responses are played through the user's speakers, all with a hands-free command line interface. The assistant uses OpenAI's Whisper API for speech-to-text conversion, OpenAI's ChatGPT API for chat response generation, and Mac OS's "say" command for text-to-speech conversion.

## Requirements

- Python 3.x
- [OpenAI API key](https://platform.openai.com/account/api-keys)

## Installation

1. Clone this repository:

```
git clone https://github.com/seanwojcik/voice-chatgpt.git
cd voice-chatgpt
```

2. (Recommended) Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

3. Install the required libraries from the `requirements.txt` file:

```
pip install -r requirements.txt
```

4. Obtain an [OpenAI API key](https://platform.openai.com/account/api-keys).

## Usage

Run the `main.py` script with your OpenAI API key. You can optionally include a system message describing the chat bot's general instructions and specify a voice:

```bash
python3 main.py <your_openai_api_key>
```

```bash
python3 main.py <you_openai_api_key> 'You are Socrates Bot. Respond to the user's messages by asking questions, challenging assumptions, and encouraging critical thinking.' -v 'Fred'
```

The application will start and prompt you to begin your voice conversation. After you speak, press Space or Enter, or after 10 seconds your speaking turn will automatically end. The application will then transcribe your speech, send the full conversation to the ChatGPT API, and play back the generated response with your system's audio output. To stop the assistant, press Esc when it is your turn to speak.

Voice options include Alex, Daniel, Fiona, Fred, Samantha, Victoria, and any other voices in Accessibility section of System Settings.

