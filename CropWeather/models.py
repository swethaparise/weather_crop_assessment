from app import db


class Weather(db.Model):
    """
    This model stores the value of weather condition on daily basis for a location throughout the year.
    """
    date = db.Column(db.String(8))
    max_temp = db.Column(db.Integer(4))
    min_temp = db.Column(db.Integer(4))
    precipitation = db.Column(db.Integer(4))
    station = db.Column(db.String(16))

    def __init__(self, date, max_temp, min_temp, precipitation, station):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.precipitation = precipitation
        self.station = station

    def serialize(self):
        return {
            'date': self.date,
            'max_temp': self.max_temp,
            'min_temp': self.min_temp,
            'precipitation' : self.precipitation,
            'station':  self.station
        }


class Crop(db.Model):
    """
    This model stores the crop data
    """
    year = db.Column(db.String(8))
    yield_per_year = db.Column(db.Integer(8))

    def __init__(self, year, yield_per_year):
        self.year = year
        self.yield_per_year = yield_per_year

    def serialize(self):
        return {
            'year': self.year,
            'yield_per_year': self.yield_per_year
        }