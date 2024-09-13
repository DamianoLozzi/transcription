import whisper
from pydub import AudioSegment
from tempfile import NamedTemporaryFile
from threading import Lock
import os


class Transcription:
    def __init__(self, model_name : str):
        self.model = whisper.load_model(model_name)
        self.lock = Lock()

    def transcribe(self, audio_file : str):
        try:
            def _transcribe(audio_file : str):
                with NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
                    audio = AudioSegment.from_file(audio_file)
                    audio.export(temp_audio_file.name, format="wav")
                with self.lock:
                    yield self.model.transcribe(temp_audio_file.name)
                    print("Transcription done")
                    temp_audio_file.close()
                    os.remove(temp_audio_file.name)
            transcription = _transcribe(audio_file)
            return next(transcription)
        except Exception as e:
            raise RuntimeError("Transcription failed") from e
