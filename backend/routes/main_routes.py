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
        path_to_remove = request.get_data().decode('utf-8')
        if not path_to_remove:
            return jsonify({"error": "No path provided"}), 400

        response = g.user.remove_library(path_to_remove)
        return jsonify({"success": True})
    except Exception as error:
        print("remove library path:", error)
        return str(error), 500

    
@main_bp.route('/getBacRecInfos', methods=['GET'])
def sendBackRecInfos():
    try:
        print("sendBacRecInfos:", g.user.get_bac_rec_infos())
        return jsonify(g.user.get_bac_rec_infos())
    except Exception as error:
        print("sendLibrariesPath:", error)

@main_bp.route('/modifyBackRecording', methods=['POST'])
def modifyBackRecording():
    try:
        raw_data = request.json
        payload = raw_data.get('payload')
        bac_rec_enabled = payload.get('bac_rec_enabled')
        bac_rec_time = payload.get('bac_rec_time')
        start_bac_rec = False
        stop_bac_rec = False

        user = g.user
        print("condition: ", g.user.bac_rec_enabled, bac_rec_enabled)
        if (g.user.bac_rec_enabled == False and bac_rec_enabled == True):
            start_bac_rec = True
        elif (g.user.bac_rec_enabled == True and bac_rec_enabled == False):
            stop_bac_rec = True

        user.bac_rec_enabled = bac_rec_enabled
        user.bac_rec_time = int(bac_rec_time)
        user.recorder.bac_rec_enabled = bac_rec_enabled
        user.recorder.bac_rec_time = int(bac_rec_time)
        user.save_user_state()

        if (start_bac_rec):
            g.user.recorder.bac_rec_activated()
        elif (stop_bac_rec):
            g.user.recorder.bac_rec_deactivated()
        
        print("user: ",user.bac_rec_enabled, user.bac_rec_time, user.recorder.bac_rec_time)

        return jsonify({"success": True, "bac_rec_enabled": bac_rec_enabled, "bac_rec_time": bac_rec_time})

    except Exception as error:
        print("Error modifying backward recording:", error)
        return jsonify({"error": str(error)}), 500 