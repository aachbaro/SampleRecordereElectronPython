import soundfile as sf
import numpy as np
import soundcard as sc
from datetime import datetime
import threading
from models import db, Sample
from flask import current_app
import time

class Recorder:

    def __init__(self, bac_rec_state, bac_rec_time):   
        # RECORDING TOOLS
        self.mic = None
        self.is_recording = False
        self.record_thread = None
        self.bac_rec_thread = None
        self.bac_rec_enabled = bac_rec_state
        self.bac_rec_time = bac_rec_time
        if (self.bac_rec_enabled):
            self.bac_rec_activated()

    def record_button_clicked(self, selected_library):
        self.selected_folder_path = selected_library
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.is_recording = True
        self.mic = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=44100)
        self.record_thread = threading.Thread(target=self.record)
        self.record_thread.start()

    def stop_recording(self):
        self.is_recording = False
        if self.record_thread:
            self.record_thread.join()

    def bac_rec_activated(self):
        print("back_rec_activated")
        self.bac_rec_thread = threading.Thread(target=self.back_recording)
        self.bac_rec_thread.start()

    def bac_rec_deactivated(self):
        print("back_rec_deactivated")
        self.bac_rec_thread.join()

    def record(self):
        output_file_name = self.create_file_name()
        sample_rate = 44100
        frames = []

        with self.mic:
            print('Recording...')
            try:
                sound_started = False
                while self.is_recording:
                    data = self.mic.record(numframes=sample_rate)
                    if np.any(data) or sound_started:
                        sound_started = True
                        frames.append(data)
            except KeyboardInterrupt:
                print("Recording interrupted by user.")

        if frames:
            self.save_recording(frames, output_file_name, sample_rate)
        else:
            print("Error: no audio recorded")

    def back_recording(self):
        print("back_rec thread launched")
        while self.bac_rec_enabled:
            print(self.bac_rec_time)
            time.sleep(1)
        print('bacRec thread stoped')

    def save_recording(self, frames, output_file_name, sample_rate):
        try:
            all_recordings = np.vstack(frames)
            sf.write(file=output_file_name, data=all_recordings, samplerate=sample_rate)
            print(f'Audio saved in {output_file_name}.')
        except Exception as error:
            print(f"Error saving audio: {error}")

    def create_file_name(self):
        maintenant = datetime.now()
        format_date_heure = maintenant.strftime("SMPL_%Y-%m-%d_%Hh%M.%S")
        if (self.selected_folder_path):
            return f"{self.selected_folder_path}/{format_date_heure}.wav"
        else:
            return f"{format_date_heure}.wav"

    def get_is_recording(self):
        return self.is_recording