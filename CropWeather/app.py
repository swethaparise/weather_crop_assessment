from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from common_config import *
from models import Weather
from views import save_weather
from views import save_crop

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DATABASE}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

# Initialising DB
db = SQLAlchemy(app)


@app.route('/api/weather')
def ingest_weather_data():
    """
    This API get the data from the file and save it in database.
    :return: json response.
    """
    try:
        save_weather()
        return jsonify({"Success": "Saved weather."})
    except:
        return jsonify({"Error": "Unable to save weather."})


@app.route('/api/yield')
def ingest_crop_yield_data():
    """
    This API save drop data to database.
    :return: response
    """
    try:
        save_crop()
        return jsonify({"Success": "Saved crop."})
    except:
        return jsonify({"Error": "Unable to save crop."})


@app.route('/api/weather/stats')
def get_statistics_data():
    """
    API to send weather statistics.
    :return: response
    """
    max_temp = (
        db.session.query(Weather)\
            .group_by(func.avg(Weather.max_temp))
    )

    min_temp = (
        db.session.query(Weather) \
            .group_by(func.avg(Weather.min_temp))
    )
    avg_per = (
        db.session.query(Weather)\
            .group_by(func.sum(Weather.precipitation))
    )

    return jsonify({'max_temp': max_temp, 'min_temp': min_temp, 'total': avg_per})


if __name__ == '__main__':
    app.run()
