from flask import Blueprint, jsonify, request, current_app, g
from models.SampleLibrary import SampleBank
from models import Recorder
import time


record_bp = Blueprint('record_bp', __name__)

@record_bp.route('/recordButtonClicked', methods=['POST'])
def recordButtonClicked():
    try:
        data = request.get_json()
        print("yeh")
        last_record_data = None
        is_recording = g.user.recorder.record_button_clicked(data.get('path'), data.get('retroTime'))            
        if not is_recording:
            print("yeh")
            while not g.user.recorder.ready_to_send_data:
                continue
            last_record_data = g.user.recorder.get_last_record_data()
            print(last_record_data)
        return jsonify(g.user.recorder.get_is_recording(), last_record_data)
    except Exception as error:
        print("Req recordButtonPressed:", error)