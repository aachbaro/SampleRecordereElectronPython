import os
from pathlib import Path
import sys
import pickle
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.sample import Sample
from models.recorder import Recorder
from models.SampleLibrary import SampleBank
from flask import current_app

class User:
    def __init__(self):
        print("Initialisation du User")
        self.sample_libraries = self.init_user_libraries()
        self.recorder = Recorder()
        print("sample_libraries: ", self.sample_libraries)

    def init_user_libraries(self):
        try:
            with open("folder_path.pkl", "rb") as file:
                print("init_user_library(): Selecting folder path")
                folder_paths = pickle.load(file)
                print("Loaded paths:", folder_paths)
                return [SampleBank(Path(path)) for path in folder_paths]
        except FileNotFoundError:
            print("init_user_library: No folder selected")
            return []

    def add_library(self, new_folder_path: str):
        try:
            print("Adding library")
            folder_path_list = [str(lib.root_path) for lib in self.sample_libraries]
            print("Current folder paths:", folder_path_list)
            if new_folder_path in folder_path_list:
                print(f"Library {new_folder_path} already exists")
                return f"Library {new_folder_path} already exists"
            folder_path_list.append(new_folder_path)
            print("Updated folder paths:", folder_path_list)
            with open("folder_path.pkl", "wb") as file:
                pickle.dump(folder_path_list, file)
            self.sample_libraries = self.init_user_libraries()
            return f"Library {new_folder_path} added successfully"
        except Exception as error:
            print("Add library:", error)
            return f"Error adding library: {error}"

    def remove_library(self, library_to_remove: str):
        try:
            print("Removing library")
            library_to_remove_path = Path(library_to_remove)
            self.sample_libraries = [lib for lib in self.sample_libraries if lib.root_path != library_to_remove_path]
            folder_path_list = [str(lib.root_path) for lib in self.sample_libraries]
            print("Updated folder paths after removal:", folder_path_list)
            with open("folder_path.pkl", "wb") as file:
                pickle.dump(folder_path_list, file)
            return f"Library {library_to_remove} removed successfully"
        except Exception as error:
            print("Remove library:", error)
            return f"There was an error removing {library_to_remove}: {error}"

    def get_sample_libraries(self):
        return self.sample_libraries

    def get_libraries_paths(self):
        return [str(lib.root_path) for lib in self.sample_libraries]

    def to_dict(self):
        return {
            'username': self.username,
            'sample_libraries': [lib.to_dict() for lib in self.sample_libraries],
            'recorder': self.recorder.to_dict(),
            'recorder_settings': self.recorder_settings.to_dict()
        }

    def __repr__(self):
        return f"sample_libraries={self.sample_libraries}"