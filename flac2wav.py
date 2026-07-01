import subprocess
import os

def process_audio(input_file, output_file):
    # -ar 44100: 44.1kHz
    # -ac 1: Mono (essential for voice cloning)
    # -af loudnorm=I=-14: LUFS normalization
    cmd = [
        "ffmpeg", "-i", input_file,
        "-ar", "44100", "-ac", "1", "-sample_fmt", "s16",
        "-af", "loudnorm=I=-14",
        output_file
    ]
    subprocess.run(cmd, check=True)

# Usage: Run on your source folder
