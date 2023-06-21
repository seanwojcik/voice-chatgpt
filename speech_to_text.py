# speech_to_text.py

import openai
import pyaudio
import wave
import keyboard
import time


def record_audio(filename, duration=None):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print("* Recording")

    frames = []
    start_time = time.time()

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        elapsed_time = time.time() - start_time
        if (
            (duration and elapsed_time >= duration)
            or keyboard.is_pressed("space")
            or keyboard.is_pressed("enter")
        ):
            break

    print("* Finished recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()


def transcribe_audio(filename, api_key=None):
    if api_key is not None:
        openai.api_key = api_key

    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript["text"]
