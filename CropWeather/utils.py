import os
import pandas as pd


def get_weather_data(path):
    """
    method to read file and return data in csv format.
    :param path:
    :return: pandas dataframe.
    """
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['date', 'max_temp', 'min_temp', 'precipitation'])


def get_crop_data(path):
    """
    method to read file and return for crop data.
    :param path:
    :return:
    """
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['year', 'yield_per_year'])
