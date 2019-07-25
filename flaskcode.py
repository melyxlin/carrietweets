from flask import Flask
from flask import jsonify
from flask import request
import test
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/translate/<string:name>', methods=['GET'])
def getTranslation(name):
    translation = test.translate(name)
    return jsonify({'message': translation})