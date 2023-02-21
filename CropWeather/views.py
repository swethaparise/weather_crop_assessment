import os

from app import db

from models import Weather
from models import Crop

from utils import get_weather_data
from utils import get_crop_data

from common_config import WEATHER_FILE_PATH, CROP_FILE_PATH


def get_filename(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]


def save_weather():
    file_path = WEATHER_FILE_PATH
    if os.path.exists(file_path):
        for file in os.listdir(file_path):
            df = get_weather_data(file)
            df['location'] = get_filename(file)
            db_value = df.to_dict(orient='records')
            weather_data = [Weather(**weather) for weather in db_value]
            try:
                db.session.add(weather_data)
                db.session.commit()
                return 'Successfully added data'
            except Exception as e:
                return 'Unable to add data'


def save_crop():
    file_path = CROP_FILE_PATH
    if os.path.exists(file_path):
        for file in os.listdir(file_path):
            df = get_crop_data(file)
            db_value = df.to_dict(orient='records')
            crop_data = [Crop(**crop) for crop in db_value]
            try:
                db.session.add(crop_data)
                db.session.commit()
                return 'Successfully added data'
            except Exception as e:
                return 'Unable to add data'


