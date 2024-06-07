from flask import Blueprint, jsonify, request, current_app
from models import Recorder

record_bp = Blueprint('record_bp', __name__)

@record_bp.route('/recordButtonClicked', methods=['POST'])
def recordButtonClicked():
    try:
        current_app.recorder.record_button_clicked()
        return current_app.recorder.get_is_recording()
    except Exception as error:
        print("Error:", error)


@record_bp.route('/selectSaveFolder', methods=['POST'])
def selectFolderPath():
    try:
        path = request.get_data().decode('utf-8')
        print(path)
        return('ok')
    except Exception as error:
        print("Error /selectSaveFolder:", error)