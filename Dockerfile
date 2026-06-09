FROM onerahmet/openai-whisper-asr-webservice:latest 

RUN pip install openai-whisper

RUN python3 -c "import whisper; whisper.load_model('base', download_root='/app/models')"

ENV ASR_MODEL=base
ENV ASR_MODEL_PATH=/app/models
ENV ASR_DEVICE=cpu