import soundfile as sf
import numpy as np
import soundcard as sc
from datetime import datetime
import threading
import pickle
from models import db, Sample
from flask import current_app



class Recorder:

    def __init__(self):   
        # RECORDING TOOLS
        self.mic = None
        self.is_recording = False
        self.record_thread = None
        self.selected_folder_path = self.load_folder_path()

    def record_button_clicked(self):
        if self.is_recording:
            self.is_recording = False
        else:
            self.is_recording = True
            self.mic = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=44100)
            self.record_thread = threading.Thread(target=self.record)
            self.record_thread.start()

    def record(self):
        OUTPUT_FILE_NAME = self.create_file_name()
        SAMPLE_RATE = 44100
        frames = []
        data = 0
        self.mic.__enter__()
        print('Recording...')
        try:
            sound_started = False
            while self.is_recording:     
                data = self.mic.record(numframes=SAMPLE_RATE)
                if np.any(data) | sound_started:
                    sound_started = True
                    frames.append(data)
        except KeyboardInterrupt:
            pass
        allrec = np.vstack(frames)
        sf.write(file=OUTPUT_FILE_NAME, data=allrec, samplerate=SAMPLE_RATE)
        print('Audio saved in %s.', OUTPUT_FILE_NAME)
        with current_app.app_context():
            new_sample = Sample(OUTPUT_FILE_NAME)
            db.session.add(new_sample)
            db.session.commit()

    def create_file_name(self):
        maintenant = datetime.now()
        format_date_heure = maintenant.strftime("SMPL_%Y-%m-%d_%Hh%M.%S")
        if (self.selected_folder_path):
            return f"{self.selected_folder_path}/{format_date_heure}.wav"
        else:
            return f"{format_date_heure}.wav"


    def save_folder_path(self):
        with open("folder_path.pkl", "wb") as file:
            pickle.dump(self.selected_folder_path, file)

    def load_folder_path(self):
        try:
            with open("folder_path.pkl", "rb") as file:
                print("load_folder_path(): Selecting folder path")
                return pickle.load(file)
        except FileNotFoundError:
            print("load_folder_path(): No folder selected")
            return None

    def set_folder_path(self, folder_path: str):
        print("method: set_folder_path()")
        self.selected_folder_path = folder_path
        self.save_folder_path()

    def get_is_recording(self):
        return self.is_recording