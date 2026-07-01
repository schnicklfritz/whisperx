FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install only the essentials
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    ffmpeg \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set up the Python virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Torch for your Blackwell-generation GPU
RUN pip install --no-cache-dir torch torchaudio --index-url https://download.pytorch.org/whl/cu128

# Install WhisperX in editable mode so you can modify it
WORKDIR /opt
RUN git clone https://github.com/m-bain/whisperX.git
WORKDIR /opt/whisperX
RUN pip install -e .

WORKDIR /workspace
CMD ["/bin/bash"]
