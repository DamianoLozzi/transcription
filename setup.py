from setuptools import setup, find_packages

setup(
    name='transcription',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai-whisper @ git+https://github.com/openai/whisper.git',
        'ffmpeg',
        'pydub',
    ],
    author='Damiano Lozzi',
    author_email='damianolozzi1989@gmail.com',
    description='A transcription tool using Whisper and Pydub',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DamianoLozzi/transcription',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)