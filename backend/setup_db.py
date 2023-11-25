import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('database/lleidahack.db')

    with open('database/schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    for i in range(10):
        value = round(i * 2.1, 2)
        cur.execute(
            "INSERT INTO plant_data (thing_id, ts, temperature, humidity, airHumidity, light) VALUES (?, ?, ?, ?, ?, ?)",
            ('plant_1', 1700926986000 + i, value, value, value, value)
        )
    for i in range(5):
        value = round(i * 1.1, 2)
        cur.execute(
            "INSERT INTO plant_data (thing_id, ts, temperature, humidity, airHumidity, light) VALUES (?, ?, ?, ?, ?, ?)",
            ('plant_2', 1700926987000 + i, value, value, value, value)
        )

    connection.commit()
    print(connection.execute('SELECT * FROM plant_data').fetchall())
    connection.close()
