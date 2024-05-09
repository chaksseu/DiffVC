import os
from tqdm import tqdm
import os
import numpy as np
from tqdm import tqdm
import sys
import torch
use_gpu = torch.cuda.is_available()

import librosa
from librosa.core import load
from librosa.filters import mel as librosa_mel_fn
mel_basis = librosa_mel_fn(22050, 1024, 80, 0, 8000)


sys.path.append('speaker_encoder/')

from encoder import inference as spk_encoder
from pathlib import Path

# loading speaker encoder
enc_model_fpath = Path('checkpts/spk_encoder/pretrained.pt') # speaker encoder path
if use_gpu:
    spk_encoder.load_model(enc_model_fpath, device="cuda")
else:
    spk_encoder.load_model(enc_model_fpath, device="cpu")

def get_mel(wav_path):
    wav, _ = load(wav_path, sr=22050)
    wav = wav[:(wav.shape[0] // 256)*256]
    wav = np.pad(wav, 384, mode='reflect')
    stft = librosa.core.stft(wav, n_fft=1024, hop_length=256, win_length=1024, window='hann', center=False)
    stftm = np.sqrt(np.real(stft) ** 2 + np.imag(stft) ** 2 + (1e-9))
    mel_spectrogram = np.matmul(mel_basis, stftm)
    log_mel_spectrogram = np.log(np.clip(mel_spectrogram, a_min=1e-5, a_max=None))
    return log_mel_spectrogram

def get_embed(wav_path):
    wav_preprocessed = spk_encoder.preprocess_wav(wav_path)
    embed = spk_encoder.embed_utterance(wav_preprocessed)
    return embed

# Set the paths to your input (wavs) and output (mels, embeds) folders
wavs_folder = "data/wavs"
mels_folder = "data/mels"
embeds_folder = "data/embeds"

# Create output folders if they don't exist
os.makedirs(mels_folder, exist_ok=True)
os.makedirs(embeds_folder, exist_ok=True)

# Assuming mel_basis and spk_encoder are defined somewhere in your code
# Make sure to load or define them before running this code

# Iterate through each speaker's folder
for speaker_folder in os.listdir(wavs_folder):
    speaker_wavs_folder = os.path.join(wavs_folder, speaker_folder)

    # Create subfolders in mels and embeds for each speaker
    speaker_mels_folder = os.path.join(mels_folder, speaker_folder)
    speaker_embeds_folder = os.path.join(embeds_folder, speaker_folder)
    os.makedirs(speaker_mels_folder, exist_ok=True)
    os.makedirs(speaker_embeds_folder, exist_ok=True)

    # Iterate through each wav file in the speaker's folder
    for wav_file in tqdm(os.listdir(speaker_wavs_folder), desc=f"Processing {speaker_folder}"):
        wav_path = os.path.join(speaker_wavs_folder, wav_file)

        # Process and save mel spectrogram
        mel_result = get_mel(wav_path)
        mel_save_path = os.path.join(speaker_mels_folder, os.path.splitext(wav_file)[0] + "_mel.npy")
        np.save(mel_save_path, mel_result)

        # Process and save speaker embedding
        embed_result = get_embed(wav_path)
        embed_save_path = os.path.join(speaker_embeds_folder, os.path.splitext(wav_file)[0] + "_embed.npy")
        np.save(embed_save_path, embed_result)
