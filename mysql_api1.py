from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def time_zone() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': '172.17.0.2',
        'port': '3306',
        'database': 'mysql'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM time_zone')
    results = [{Time_zone_id: Use_leap_seconds} for (Time_zone_id, Use_leap_seconds) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'time_zone': time_zone()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
