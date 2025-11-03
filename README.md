# SpeechToText - Wav2Vec2 Basic STT

## Objective
A simple Speech-to-Text system using the pre-trained Wav2Vec2 model from Hugging Face.
Transcribes short audio clips (WAV, mono, 16 kHz recommended) and outputs text.

## Files
- `speech_to_text.py` : main script
- `sample.wav` : example audio file (replace with your own)
- `output.txt` : transcription output (generated)
- `requirements.txt` : Python dependencies

## Setup
1. Create and activate virtual environment:
   - `python3 -m venv stt-env`
   - `source stt-env/bin/activate` (Windows: `.\stt-env\Scripts\activate`)

2. Install packages:
   - `pip install -r requirements.txt`

3. Prepare audio:
   - Ensure WAV, mono, 16kHz. Use ffmpeg to convert if needed:
     `ffmpeg -i input.mp3 -ac 1 -ar 16000 sample.wav`

## Usage
