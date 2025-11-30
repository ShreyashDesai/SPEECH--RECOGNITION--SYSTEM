🧠 Speech-to-Text System
--
👨‍💻 Internship Project — CodTech IT Solutions
--

Intern Name: Shreyash Nhanu Desai

Intern ID: CT04DR1291

Domain: Artificial Intelligence

Duration: 1st November – 1st December (4 Weeks)

Mentor: Neela Santosh

<div align="center"> <img width="100%" alt="Speech-to-Text System" src="https://github.com/user-attachments/assets/829776f9-82ea-4e41-8d6c-b3481698b43c" /> </div>
📘 Project Overview

The Speech-to-Text System is an AI-based application that converts spoken audio into written text using Automatic Speech Recognition (ASR).

It uses Wav2Vec2, a transformer-based model created by Facebook AI Research (FAIR). This model learns directly from raw audio and provides high transcription accuracy.

This intern project demonstrates skills in:

Deep Learning

Natural Language Processing (NLP)

Audio Signal Processing

Python-based AI model integration

🚀 Key Features
Feature	Description
🎯 Accurate Speech Recognition	Converts speech to text with high precision
🤖 Wav2Vec2 Model	Uses facebook/wav2vec2-base-960h
🔌 Offline Processing	Works offline after initial model download
🌍 Accent Support	Supports clear English speech and accents
💾 Auto Save	Transcription automatically saved to output.txt
🔊 Audio Requirement	Accepts mono 16kHz WAV files
🛠️ Technologies & Tools
Category	Tools / Libraries
Language	Python 3.9+
Deep Learning Framework	PyTorch
Model	Wav2Vec2
Audio Processing	librosa, soundfile, ffmpeg
IDE	Visual Studio Code
Version Control	Git & GitHub
⚙️ System Requirements
Requirement	Description
Python	Version 3.9+ (64-bit)
Git	Must be added to PATH
FFmpeg	Required for audio conversion and loading
VS Code	Recommended coding environment
🪜 Installation & Setup Guide
Step 1️⃣ — Install Prerequisites
✔ Install Python

Enable: Add Python to PATH

✔ Install Git

Enable: Add Git to PATH

✔ Install FFmpeg

Verify installation:

ffmpeg -version

Step 2️⃣ — Clone the Repository
git clone https://github.com/ShreyashDesai/Speech-To-Text-System.git
cd Speech-To-Text-System

Step 3️⃣ — Install Required Libraries
pip install torch transformers librosa soundfile


If audio errors occur:

pip install ffmpeg-python

🎤 Creating / Importing Audio Samples

You must use mono, 16kHz WAV audio.

Option 1 — Record Using Windows Voice Recorder

Open Voice Recorder

Record your audio

Save as sample.wav

Move it to the project folder

Option 2 — Convert MP3 to WAV
ffmpeg -i input.mp3 -ac 1 -ar 16000 sample.wav

Option 3 — Record Audio Using Python
import sounddevice as sd
import wavio

duration = 5
fs = 16000

print("🎙️ Recording...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
wavio.write("sample.wav", recording, fs, sampwidth=2)
print("✅ Saved as sample.wav")


Install dependencies:

pip install sounddevice wavio

▶️ How to Run the Program

Run the script using:

python speech_to_text.py --input sample.wav --output output.txt

📝 Example Output
Input Audio

🎧 sample.wav — “Hello, this is my CodTech internship project.”

Transcribed Text

🧾 hello this is my codtech internship project

🧠 Model Information
Detail	Information
Model Name	facebook/wav2vec2-base-960h
Architecture	Transformer-based ASR
Developed By	Facebook AI Research (FAIR)
Purpose	Speech representation & transcription
👨‍💻 Author

Name: Shreyash Nhanu Desai
Role: AI Intern — CodTech IT Solutions
Email: shreyashsn.desai@gmail.com

🔗 GitHub: https://github.com/ShreyashDesai

🔗 LinkedIn: https://linkedin.com/in/shreyash-desai-a13730384

🏁 Acknowledgements

I express my gratitude to CodTech IT Solutions and Mentor Neela Santosh for their constant support.
This project improved my knowledge in:

Speech Recognition

Deep Learning Architectures

Model Deployment

Audio Signal Processing

⚠️ Troubleshooting Guide
Issue	Solution
'pip' is not recognized	Reinstall Python & enable PATH
'git' is not recognized	Reinstall Git with PATH enabled
ModuleNotFoundError: torch	Run → pip install torch transformers
ffmpeg not found	Install FFmpeg and add to PATH
OSError: -9996 Invalid input device	Select another microphone or check device

