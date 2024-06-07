from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def welcome():
    return "Connected to python server"

@main_bp.route('/ping', methods=['GET'])
def ping():
    return "pong", 200