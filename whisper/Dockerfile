FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -c "import whisper; whisper.load_model('medium', download_root='/app/models')"

COPY harvard.wav .

COPY main.py .