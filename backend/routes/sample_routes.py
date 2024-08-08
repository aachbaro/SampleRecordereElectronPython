# backend/routes/sample_route.py

from flask import Blueprint, jsonify, request, g, current_app, send_from_directory
from models import db, Sample
from models.SampleLibrary import SampleBank
import os

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
def sendSampleLibrary(filename):
    try:
        # Spécifiez le répertoire où les fichiers audio sont stockés
        audio_directory = 'C:/Users/adama/Desktop/musique/librarypascuans/movies'
        
        # Retournez le fichier audio
        return send_from_directory(audio_directory, filename)
    except Exception as error:
        return str(error), 500
    
@sample_bp.route('/audio', methods=['GET'])
def serve_audio():
    try:
        # Récupérer les paramètres de requête
        directory_path = request.args.get('directoryPath')
        filename = request.args.get('filename')

        # Sécurisation et envoi du fichier
        return send_from_directory(directory_path, filename)
    except Exception as error:
        return str(error), 500
    
@sample_bp.route('/deleteAudio', methods=['DELETE'])
def delete_audio():
    try:
        filepath = request.args.get('filePath')
        print("delete: ", filepath)
        g.user.delete_sample_from_history(filepath)
        os.remove(filepath)
        print(f"{filepath} a été supprimé avec succès.")
        return jsonify(g.user.sample_history)
    except FileNotFoundError:
        print(f"Le fichier {filepath} n'existe pas.")
        return jsonify(g.user.sample_history)
    except PermissionError:
        print(f"Permission refusée pour supprimer {filepath}.")
        return jsonify(g.user.sample_history)
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier {filepath}: {e}")
        return jsonify(g.user.sample_history)