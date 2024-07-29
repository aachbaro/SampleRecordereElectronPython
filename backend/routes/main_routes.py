from flask import Blueprint, jsonify, request, current_app, g
from models.SampleLibrary import SampleBank
from models.User import User
from models import Recorder

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def welcome():
    return "Connected to python server"

@main_bp.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

@main_bp.route('/selectSaveFolder', methods=['POST'])
def selectFolderPath():
    try:
        print("add library")
        path = request.get_data().decode('utf-8')
        # g.user.recorder.set_folder_path(path)
        response = g.user.add_library(path)
        print(path)

        return(jsonify(response))
    except Exception as error:
        print("Error /selectSaveFolder:", error)

@main_bp.route('/getLibrariesPaths', methods=['GET'])
def sendLibrariesPaths():
    try:
        print("sendLibraryPaths:", g.user.get_libraries_paths())
        return jsonify(g.user.get_libraries_paths())
    except Exception as error:
        print("sendLibrariesPath:", error)

@main_bp.route('/removeLibraryPath', methods=['POST'])
def removeLibraryPath():
    try:
        print("remove library path")
        data = request.get_json()
        print(data)
        path_to_remove = data.get('path')
        if not path_to_remove:
            return jsonify({"error": "No path provided"}), 400

        response = g.user.remove_library(path_to_remove)
        return jsonify({"success": True})
    except Exception as error:
        print("remove library path:", error)
        return str(error), 500