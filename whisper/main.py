#!/usr/bin/env -S python3 -u

from faster_whisper import WhisperModel
from antithesis.lifecycle import (
    setup_complete,
)

MODEL_SIZE = "medium"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"
MODEL_DIR = "/app/models"

model = WhisperModel(
    MODEL_SIZE,
    device=DEVICE,
    compute_type=COMPUTE_TYPE,
    download_root=MODEL_DIR,
    local_files_only=True)

setup_complete("[antithesis-whisper]: model has loaded")

while True:
    segments, info = model.transcribe("harvard.wav", beam_size=5)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))