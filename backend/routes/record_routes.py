from flask import Blueprint, jsonify, request, current_app, g
from models.SampleLibrary import SampleBank
from models import Recorder


record_bp = Blueprint('record_bp', __name__)

@record_bp.route('/recordButtonClicked', methods=['POST'])
def recordButtonClicked():
    try:
        data = request.get_json()
        print(data.get('retroTime'))
        g.user.recorder.record_button_clicked(data.get('path'), data.get('retroTime'))            
        return jsonify(g.user.recorder.get_is_recording())
    except Exception as error:
        print("Req recordButtonPressed:", error)