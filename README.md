# 🧠 Speech-to-Text System  
### 👨‍💻 Internship Project — CodTech IT Solutions

**Intern Name:** Shreyash Nhanu Desai  
**Intern ID:** CT04DR1291  
**Domain:** Artificial Intelligence  
**Duration:** 1st November – 1st December  
**Mentor:** Neela Santosh  

---

## 📘 Project Overview  
The **Speech-to-Text System** is an AI-powered application that converts audio into text using **Automatic Speech Recognition (ASR)**.

This project uses **Wav2Vec2**, a transformer-based neural model developed by **Facebook AI Research (FAIR)**.  
It can learn directly from raw audio and provides high-accuracy transcription.

### This internship project demonstrates skills in:
- Deep Learning  
- NLP (Natural Language Processing)  
- Audio Signal Processing  
- Model Integration with Python  

---

## 🚀 Key Features

| Feature | Description |
|--------|-------------|
| 🎯 Accurate Speech Recognition | Converts speech to text with high precision |
| 🤖 Wav2Vec2 Model | Uses **facebook/wav2vec2-base-960h** |
| 🔌 Offline Processing | Works offline after initial model download |
| 🌍 Accent Support | Supports clear English accents |
| 💾 Auto Save | Automatically saves transcription to output.txt |
| 🔊 Audio Requirement | Requires mono, 16kHz WAV files |

---

## 🛠️ Technologies & Tools

| Category | Tools / Libraries |
|---------|-------------------|
| Language | Python 3.9+ |
| Framework | PyTorch |
| Model | Wav2Vec2 |
| Audio Processing | librosa, soundfile, ffmpeg |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

## ⚙️ System Requirements

| Requirement | Description |
|------------|-------------|
| Python | Version 3.9+ (64-bit) |
| Git | Must be added to PATH |
| FFmpeg | Required for audio conversion |
| RAM | Minimum 4GB recommended |

---

# 📥 Installation Guide (Step-by-Step & Beginner Friendly)

## 1️⃣ Download & Install Required Software

### ✔ Python (Official)
🔗 https://www.python.org/downloads/  
During installation → Check: **Add Python to PATH**

---

### ✔ Git (Official)
🔗 https://git-scm.com/downloads  
During installation → Check: **Add Git to PATH**

---

### ✔ FFmpeg (Official Builds)
🔗 https://www.gyan.dev/ffmpeg/builds/  
Download **ffmpeg-gessentials.zip**  
Extract → rename folder to **ffmpeg** → move to `C:\ffmpeg`

Add this to PATH:
C:\ffmpeg\bin

makefile
Copy code

Verify:
ffmpeg -version

yaml
Copy code

---

### ✔ Visual Studio Code (Recommended)
🔗 https://code.visualstudio.com/download

---

## 2️⃣ Clone the Project

```bash
git clone https://github.com/ShreyashDesai/SPEECH--RECOGNITION--SYSTEM
cd Speech-To-Text-System
3️⃣ Install Python Dependencies
bash
Copy code
pip install torch transformers librosa soundfile ffmpeg-python sounddevice wavio
🎤 Preparing Audio Samples
Option 1 — Record Using Windows Voice Recorder
Open Voice Recorder

Save as sample.wav

Move it to the project folder

Option 2 — Convert MP3 to WAV (16kHz Mono)
bash
Copy code
ffmpeg -i input.mp3 -ac 1 -ar 16000 sample.wav
Option 3 — Record Audio Using Python
python
Copy code
import sounddevice as sd
import wavio

duration = 5
fs = 16000

print("🎙️ Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
wavio.write("sample.wav", audio, fs, sampwidth=2)
print("✅ Saved as sample.wav")
▶️ How to Run the Program
bash
Copy code
python speech_to_text.py --input sample.wav --output output.txt
📄 Example Output
Input Audio:
🎧 “Hello, this is my CodTech internship project.”

Transcription Output:

kotlin
Copy code
hello this is my codtech internship project
🧠 Model Information
Detail	Information
Model Used	facebook/wav2vec2-base-960h
Architecture	Transformer
Developed By	Facebook AI Research (FAIR)
Purpose	Speech Representation + Speech-to-Text

👨‍💻 Author
Name: Shreyash Nhanu Desai
Role: AI Intern — CodTech IT Solutions
📧 Email: shreyashsn.desai@gmail.com
🔗 GitHub: https://github.com/ShreyashDesai
🔗 LinkedIn: https://linkedin.com/in/shreyash-desai-a13730384

🏁 Acknowledgements
I am grateful to CodTech IT Solutions and Mentor Neela Santosh for their support.
This project enhanced my knowledge in:

Speech Recognition

Deep Learning

Audio Signal Processing

Transformer Architectures

⚠️ Troubleshooting Guide
Issue	Solution
pip not recognized	Reinstall Python with Add to PATH
git not recognized	Reinstall Git with Add to PATH
ModuleNotFoundError	Run: pip install torch transformers
ffmpeg not found	Add C:\ffmpeg\bin to PATH
OSError -9996	Change microphone or input device

