from setuptools import setup, find_packages
import os

def parse_requirements(filename):
    """ Load requirements from a pip requirements file. """
    with open(filename, "r") as file:
        return file.read().splitlines()

requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_requires = parse_requirements(requirements_path) if os.path.exists(requirements_path) else [
    "deemix",
    "fairseq==0.12.2",
    "faiss-cpu==1.7.3",
    "ffmpeg-python>=0.2.0",
    "gradio==3.39.0",
    "lib==4.0.0",
    "librosa==0.9.1",
    "numpy==1.23.5",
    "onnxruntime_gpu",
    "praat-parselmouth>=0.4.2",
    "pedalboard==0.7.7",
    "pydub==0.25.1",
    "pyworld==0.3.4",
    "requests==2.31.0",
    "scipy==1.11.1",
    "soundfile==0.12.1",
    "torch==2.0.1+cu118 --find-links https://download.pytorch.org/whl/torch_stable.html",
    "torchcrepe==0.0.20",
    "tqdm==4.65.0",
    "yt_dlp==2023.7.6",
    "sox==1.4.1"
]

setup(
    name="aicovergen",
    version="1.0.0",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "aicovergen=aicovergen.main:main",
        ],
    },
)
