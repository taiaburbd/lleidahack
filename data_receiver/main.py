import json
import sqlite3
from datetime import datetime

import paho.mqtt.client as mqtt

DATABASE = '../backend/database/lleidahack.db'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = dict_factory
    return db


def on_message(client, userdata, message):
    try:
        message_string = str(message.payload.decode("utf-8"))
        print("message received ", message_string)
        print("message topic=", message.topic)
        payload = json.loads(message_string)
        connection = get_db()
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO plant_data (thing_id, ts, temperature, humidity, airHumidity, light) VALUES (?, ?, ?, ?, ?, ?)",
            (payload["id"], int(datetime.now().timestamp()*1000), payload["temperature"], payload["soil_humidity"],
             payload["air_humidity"],
             payload["light"])
        )

        connection.commit()
        connection.close()
    except Exception as X:
        print(X)
        print("Not good message:", str(message.payload.decode("utf-8")))


def on_log(client, userdata, level, buf):
    print("log: ", buf)


if __name__ == '__main__':
    client_name = 'PyCharm'
    broker_address = "84.88.76.18"
    port = 1883
    username = "batallon_cosechador"
    password = "C05ech@d0r!"
    base_topic = "hackeps"
    staff_topic = f"{base_topic}/eurecat"
    team_topic = f"{base_topic}/BC"

    client = mqtt.Client(client_name)
    # client.on_connect = on_connect
    # client.on_log = on_log
    client.on_message = on_message
    client.username_pw_set(username, password)
    client.connect(broker_address, port)
    # client.loop_start()  # start the loop

    print("Subscribing to topic", staff_topic)
    client.subscribe(staff_topic)
    print("Subscribing to topic", team_topic)
    client.subscribe(team_topic)
    client.loop_forever()  # stop the loop
