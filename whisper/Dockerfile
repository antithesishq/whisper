FROM onerahmet/openai-whisper-asr-webservice:latest 

RUN pip install openai-whisper

RUN python3 -c "import whisper; whisper.load_model('medium', download_root='/app/models')"

ENV ASR_MODEL=medium
ENV ASR_MODEL_PATH=/app/models
ENV ASR_DEVICE=cpu