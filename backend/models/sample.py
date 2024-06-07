import numpy as np
import wave
import os
import datetime
import base64
from . import db

class Sample(db.Model):
    """A class that stores data about a sample."""
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    # creation_date = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    frame_list = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, path: str):
        self.path = path
        self.name = self.extract_name_from_path()
        # self.creation_date = self.get_creation_date()
        self.frame_list, self.duration = self.extract_data_from_wav()

    def extract_name_from_path(self) -> str:
        """Extracts the name of the sample from its path."""
        file_name = os.path.basename(self.path)  # Cross-platform compatibility
        return os.path.splitext(file_name)[0]  # Remove the extension

    def extract_data_from_wav(self) -> tuple:
        """Extracts frame data and duration from a WAV file."""
        with wave.open(self.path, 'rb') as wav_file:
            # Extract frame data
            frame_list = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
            # Extract duration
            framerate = wav_file.getframerate()
            nframes = wav_file.getnframes()
            duration = nframes / framerate
        return frame_list.tobytes(), duration  # Store as binary data

    # def get_creation_date(self) -> str:
    #     """Returns the creation date of the sample in the desired format."""
    #     creation_timestamp = os.path.getctime(self.path)
    #     creation_datetime = datetime.fromtimestamp(creation_timestamp)
    #     return creation_datetime.strftime("%y/%m/%d-%HH%MM")

    def __str__(self):
        return f"name: {self.name}\nduration: {self.duration}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'path': self.path,
            'name': self.name,
            'duration': self.duration,
            'frame_list': base64.b64encode(self.frame_list).decode('utf-8')
            # 'frame_list': self.frame_list,
        }