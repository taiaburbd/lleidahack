import json
import sqlite3
from flask_cors import CORS

from flask import Flask, g, request, Response
from flask import jsonify
from markupsafe import escape

DATABASE = './database/lleidahack.db'
app = Flask(__name__)
CORS(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # db.row_factory = sqlite3.Row
        db.row_factory = dict_factory
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/plants', methods=['GET'])
def get_plants_summary():
    query = f'SELECT distinct thing_id FROM plant_data group by thing_id'
    conn = get_db()
    data_points = conn.execute(query).fetchall()
    conn.close()
    return jsonify(data_points)


@app.route('/plant/<plant_id>/summary', methods=['GET'])
def get_plant_summary(plant_id):
    query = f'SELECT * FROM plant_data where thing_id="{plant_id}" ORDER BY ts DESC LIMIT 1'
    conn = get_db()
    data_point = conn.execute(query).fetchone()
    conn.close()

    url = 'http://localhost:5001/prediction/watering'
    print(data_point)
    response = requests.post(url, json=json.dumps([data_point]))
    response = json.loads(response.content)
    data_point["prediction"] = response[0]
    if data_point:
        return jsonify(data_point)
    else:
        return jsonify({}), 404


@app.route('/plant/<plant_id>/detail', methods=['GET'])
def get_plant_detail(plant_id):
    query = f'SELECT * FROM plant_data where thing_id="{plant_id}" ORDER BY ts ASC'
    if "limit" in request.args.keys():
        query += f' LIMIT {request.args.get("limit")}'
    conn = get_db()
    data_points = conn.execute(query).fetchall()
    conn.close()
    return Response(json.dumps(data_points), mimetype="application/json")


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
