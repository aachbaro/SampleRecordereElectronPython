from flask import Blueprint, jsonify, request, current_app, g
from models.SampleLibrary import SampleBank
from models import Recorder


record_bp = Blueprint('record_bp', __name__)

@record_bp.route('/recordButtonClicked', methods=['POST'])
def recordButtonClicked():
    try:
        data = request.get_json()
        g.user.recorder.record_button_clicked(data.get('path'))            
        return jsonify(g.user.recorder.get_is_recording())
    except Exception as error:
        print("Req recordButtonPressed:", error)


# @record_bp.route('/selectSaveFolder', methods=['POST'])
# def selectFolderPath():
#     try:
#         path = request.get_data().decode('utf-8')
#         g.user.recorder.set_folder_path(path)
#         # g.sampleBank.set_folder_path(path)
#         print(path)

#         return('ok')
#     except Exception as error:
#         print("Error /selectSaveFolder:", error)