from flask import Flask, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from models import db, Recorder, SampleLibrary
from models.SampleLibrary import SampleBank
from routes.main_routes import main_bp
from routes.sample_routes import sample_bp
from routes.record_routes import record_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///samples.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

recorder = Recorder()
sampleBank = SampleBank()

CORS(app, resources={r"/*": {'origins': "http://localhost:8080"}})

# Enregistrer les Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(sample_bp)
app.register_blueprint(record_bp)

@app.before_request
def before_request():
    g.recorder = recorder
    g.sampleBank = sampleBank


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)