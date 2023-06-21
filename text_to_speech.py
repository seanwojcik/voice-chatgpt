# text_to_speech.py

import pygame

# from IPython.display import Audio
from gtts import gTTS


def text_to_speech(text, filename):
    tts = gTTS(text=text, lang="en-GB")
    tts.save(filename)


def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
