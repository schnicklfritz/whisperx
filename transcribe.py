import whisperx
import os
import json

# Settings
device = "cuda"
batch_size = 2
audio_dir = "/workspace/data"
output_file = "/workspace/data/transcripts.json"

# Load Model
model = whisperx.load_model("large-v3", device, compute_type="float16")

results = {}

for filename in os.listdir(audio_dir):
    if filename.endswith(".wav"):
        print(f"Processing {filename}...")
        audio = whisperx.load_audio(os.path.join(audio_dir, filename))
        result = model.transcribe(audio, batch_size=batch_size)
        
        # Store segments without standard normalization formatting
        results[filename] = result["segments"]

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)
print("Done.")
