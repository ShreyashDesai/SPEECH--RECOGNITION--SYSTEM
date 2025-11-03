import argparse
import librosa
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# ----------------------------
# Load and preprocess audio
# ----------------------------
def load_audio(path, target_sr=16000):
    """
    Load audio file and resample to 16kHz mono using librosa.
    """
    speech_array, sr = librosa.load(path, sr=target_sr, mono=True)
    return np.array(speech_array), sr

# ----------------------------
# Transcribe function
# ----------------------------
def transcribe(audio_path, model_name="facebook/wav2vec2-base-960h"):
    print("🔹 Loading model... This may take a few seconds.")
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)

    print("🎧 Loading and processing audio...")
    speech, sr = load_audio(audio_path)
    input_values = processor(speech, sampling_rate=sr, return_tensors="pt", padding=True).input_values

    print("🧠 Transcribing...")
    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return transcription.lower()

# ----------------------------
# Main execution
# ----------------------------
def main():
    parser = argparse.ArgumentParser(description="Speech-to-Text using Wav2Vec2")
    parser.add_argument("--input", type=str, required=True, help="Path to input audio file (WAV, 16kHz)")
    parser.add_argument("--output", type=str, default="output.txt", help="Path to save transcription")
    parser.add_argument("--model", type=str, default="facebook/wav2vec2-base-960h", help="Model name")
    args = parser.parse_args()

    text = transcribe(args.input, model_name=args.model)

    print("\n✅ Transcription completed successfully!\n")
    print("🗒️  Transcribed Text:\n")
    print(text)
    print("\n💾 Saved to:", args.output)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
