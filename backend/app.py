from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"http://localhost:8080"}})


@app.route('/')
def Welcome():
    return "Connected to python server"

@app.route('/ping', methods=['GET'])
def ping():
    return "pong pong", 200

if __name__ == '__main__':
    app.run(debug=True)