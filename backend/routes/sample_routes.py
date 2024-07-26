# backend/routes/sample_route.py

from flask import Blueprint, jsonify, request, g, current_app
from models import db, Sample
from models.SampleLibrary import SampleBank

sample_bp = Blueprint('sample_bp', __name__)

@sample_bp.route('/upload', methods=['POST'])
def upload_file():
    try:
        path = request.get_data().decode('utf-8')
        new_sample = Sample(path)
        db.session.add(new_sample)
        db.session.commit()
        samples = Sample.query.all()
        sample_list = [sample.to_dict() for sample in samples]
        return jsonify(sample_list)
    except Exception as error:
        return str(error), 500
    
@sample_bp.route('/getSampleLibrary', methods=['GET'])
def sendSampleLibrary():
    try:
        # samples = Sample.query.all()
        # sample_list = [sample.to_dict() for sample in samples]
        sample_list = g.sampleBank.to_dict()
        print(sample_list)
        return jsonify(sample_list)
    except Exception as error:
        return str(error), 500