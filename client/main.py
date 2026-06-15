#!/usr/bin/env -S python3 -u


import sys
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

total_transcriptions = 0

def transcribe_audio():
    global total_transcriptions
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

    total_transcriptions += 1
    print(response.text)


if __name__ == "__main__":
    setup_complete("[client]: whisper server is ready")
    if len(sys.argv) > 1:
        run_len = sys.argv[1]
        print(f"[client]: running for {run_len} (sec)")
        if run_len == "inf":
            while True:
                transcribe_audio()
                time.sleep(10)
        else:
            start_time = time.time()
            run_len = int(run_len)
            while time.time() - start_time <= run_len:
                transcribe_audio()
                time.sleep(10)
            print(f"[client]: total transcriptions {total_transcriptions}")
    else:
        print("run length arg not provided")
        exit(1)
