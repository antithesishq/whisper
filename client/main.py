#!/usr/bin/env -S python3 -u


import time
import requests
import hashlib
from antithesis import random
from antithesis.lifecycle import (
    setup_complete,
)
from antithesis.assertions import (
    always
)


def transcribe_audio():
    url = 'http://antithesis-whisper:9000/asr'
    params = {
        'encode': 'true',
        'task': 'transcribe',
        'initial_prompt': 'transcribe the audio',
        'output': 'txt'
    }
    headers = {
        'accept': 'application/json'
    }

    files = {
        'audio_file': open('harvard.wav', 'rb')
    }

    try:
        response = requests.post(url, params=params, headers=headers, files=files)
        response.raise_for_status()
    except Exception as e:
        print(f"[client]: transcribing audio failed {e}")

    print(response.text)



if __name__ == "__main__":
    setup_complete("[client]: whisper server is ready")
    while True:
        transcribe_audio()
        time.sleep(10)
