import os
from pathlib import Path
import sys
import pickle
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.sample import Sample
from flask import current_app

class Folder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.name = self.folder_path.name
        self.contents = []
        self.is_directory = True

    def __repr__(self):
        contents_str = "\n".join([repr(item) for item in self.contents])
        return f"SampleBank(root_path={self.folder_path}, contents=[\n{self.name, contents_str}\n])"

    def to_dict(self):
        return {
            'name': self.name,
            'path': str(self.folder_path),
            'contents': [item.to_dict() for item in self.contents]
        }

class SampleBank:
    def __init__(self, root_path=None, id=0):
        print("init sample bank")
        self.id = id
        if (root_path):
            self.root_path = Path(root_path)
        else:
            self.root_path = Path(self.load_folder_path())
        self.contents = self._build_contents(self.root_path)

    def _build_contents(self, current_path):
        contents = []
        for entry in current_path.iterdir():
            if entry.is_file() and entry.suffix == '.wav':
                contents.append(Sample(str(entry)))
            elif entry.is_dir():
                folder = Folder(entry)
                folder.contents = self._build_contents(entry)
                contents.append(folder)
        return contents
    
    def set_root_path(self, new_root_path: str):
        self.root_path = new_root_path

    def get_root_path(self):
        return self.root_path

    def load_folder_path(self):
        try:
            with open("folder_path.pkl", "rb") as file:
                print("load_folder_path(): Selecting folder path")
                return pickle.load(file)
        except FileNotFoundError:
            print("load_folder_path(): No folder selected")
            return None

    def __repr__(self):
        contents_str = "\n".join([repr(item) for item in self.contents])
        return f"SampleBank(root_path={self.root_path}, contents=[\n{contents_str}\n])"

    def to_dict(self):
        print("SampleBank.to_dict")
        return {
            'root_path': str(self.root_path),
            'contents': [item.to_dict() for item in self.contents],
            'is_directory': True
        }
    
# root_dir = "C:/Users/adama/Desktop/musique/librarypascuans/synth"
# sample_bank = SampleBank(root_dir)

# print(sample_bank.to_dict())