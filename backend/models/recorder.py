import soundfile as sf
import numpy as np
import soundcard as sc
from datetime import datetime
import threading
from queue import Queue, Empty
import time

class Recorder:

    def __init__(self, bac_rec_state: int, bac_rec_time: int): 
        # RECORDING TOOLS
        self.mic = None
        self.is_recording = False
        self.record_thread = None
        self.bac_rec_thread = None
        self.save_thread = None
        self.bac_rec_enabled = bac_rec_state
        self.bac_rec_time = bac_rec_time
        self.retro_time_selected = 0
        self.last_audio_recorded_name = None
        self.last_audio_recorded_frames = []
        self.ready_to_send_data = False
        if self.bac_rec_enabled:
            self.bac_rec_activated()

    def record_button_clicked(self, selected_library, retro_time_selected):
        self.selected_folder_path = selected_library
        self.retro_time_selected = retro_time_selected
        if self.is_recording:
            return self.stop_recording()
        else:
            return self.start_recording()

    def start_recording(self):
        self.is_recording = True
        if not self.bac_rec_enabled:
            self.mic = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=44100)
            self.record_thread = threading.Thread(target=self.record)
            self.record_thread.start()
        return True

    def stop_recording(self):
        self.is_recording = False
        if self.record_thread:
            self.record_thread.join()
        if self.bac_rec_thread:
            self.bac_rec_thread.join()
        self.save_recording(self.last_audio_recorded_frames, self.last_audio_recorded_name, 44100)
        if self.bac_rec_enabled:
            self.bac_rec_activated()
        return False


    def bac_rec_activated(self):
        print("recorder: back_rec_activated")
        self.mic = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=44100)
        self.bac_rec_thread = threading.Thread(target=self.back_recording)
        self.bac_rec_thread.start()

    def bac_rec_deactivated(self):
        print("recorder: back_rec_deactivated")
        self.bac_rec_thread.join()

    def record(self):
        output_file_name = self.create_file_name()
        sample_rate = 44100
        frames = []

        with self.mic:
            print('recorder: Recording...')
            try:
                sound_started = False
                while self.is_recording:
                    data = self.mic.record(numframes=sample_rate)
                    if np.any(data) or sound_started:
                        sound_started = True
                        frames.append(data)
            except KeyboardInterrupt:
                print("recorder: Recording interrupted by user.")

        if frames:
            self.last_audio_recorded_frames = frames
            self.last_audio_recorded_name = output_file_name
        else:
            print("Error: no audio recorded")

    def back_recording(self):
        print("recorder: back_rec thread launched")
        sample_rate = 44100
        pre_frames = []
        frames = []
        i = 0
        try:
            with self.mic:
                sound_started = False
                record_started = False
                while self.bac_rec_enabled:
                    if not record_started and self.is_recording:
                        record_started = True
                        print('recorder: Recording...')
                        output_file_name = self.create_file_name()
                    elif not self.is_recording and record_started:
                        print("recorder: record stopped from bac_rec_thread")
                        record_started = False
                        sound_started = False
                        if self.retro_time_selected > 0:
                            pre_frames = pre_frames[-self.retro_time_selected:]
                        self.last_audio_recorded_frames = pre_frames + frames
                        self.last_audio_recorded_name = output_file_name
                        frames.clear()
                        pre_frames.clear()
                        break

                    data = self.mic.record(numframes=sample_rate)
                    if np.any(data) or sound_started:
                        sound_started = True
                        if record_started:
                            frames.append(data)
                        else:
                            pre_frames.append(data)
                            if len(pre_frames) > self.bac_rec_time:
                                pre_frames.pop(0)
        except KeyboardInterrupt:
            print("recorder: Recording interrupted by user.")
        print('recorder: bacRec thread stopped')

    def save_recording(self, frames, output_file_name, sample_rate):
        try:
            all_recordings = np.vstack(frames)
            sf.write(file=output_file_name, data=all_recordings, samplerate=sample_rate)
            print(f'recorder: Audio saved in {output_file_name}.')
            self.ready_to_send_data = True
        except Exception as error:
            print(f"recorder: Error saving audio: {error}")
            self.ready_to_send_data = True

    def create_file_name(self):
        maintenant = datetime.now()
        format_date_heure = maintenant.strftime("SMPL_%Y-%m-%d_%Hh%M.%S")
        if self.selected_folder_path:
            return f"{self.selected_folder_path}/{format_date_heure}.wav"
        else:
            return f"{format_date_heure}.wav"
        
    def get_last_record_data(self):
        filename = self.last_audio_recorded_name
        frames = self.last_audio_recorded_frames
        date = datetime.now()
        length = len(frames)
        self.ready_to_send_data = True
        recording_info = {
            "filename": filename,
            "date": date,
            "length": length,
        }
        return recording_info

    def get_is_recording(self):
        return self.is_recording
