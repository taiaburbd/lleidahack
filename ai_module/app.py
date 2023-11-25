import json

from flask import Flask, Response, request
from markupsafe import escape

from ai import WateringPredictor

DATABASE = './database/lleidahack.db'
app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/plants/ids', methods=['POST'])
def generate_watering_prediction():
    data = request.get_json()
    predictor = WateringPredictor()
    predictions = [predictor.generate_prediction(item) for item in data]
    return Response(json.dumps(predictions), mimetype="application/json")


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
