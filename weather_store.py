# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as xml
import json
import pytz
from datetime import datetime, timedelta
from StringIO import StringIO
from pprint import pprint

class WeatherStore():

    def __init__(self, city):
        self.city = city
        self.url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + self.city

    def get_weather_description(self):
        r = requests.get(self.url)
        weather = json.load(StringIO(r.content))
        return weather.get('description').get('text')

    def get_weather_today(self):
        # TODO timedelta 以外は同じなのでまとめる
        today = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d')
        r = requests.get(self.url)
        weather = json.load(StringIO(r.content))
        for data in weather.get('forecasts'):
            if today == data.get('date'):
                message = []
                message.append(today)
                message.append(u'forecasts:' + data.get('image').get('title'))
                temperature_max = data.get('temperature').get('max')
                if temperature_max and temperature_max.get('celsius'):
                    message.append(u'max celsius:' + temperature_max.get('celsius'))
                temperature_min = data.get('temperature').get('min')
                if temperature_min and temperature_min.get('celsius'):
                    message.append(u'min celsius:' + temperature_min.get('celsius'))
                return " ".join(message)

    def get_weather_tomorrow(self):
        # TODO timedelta 以外は同じなのでまとめる
        today = datetime.now(pytz.timezone('Asia/Tokyo'))
        days = timedelta(days = 1)
        tomorrow = (today + days).strftime('%Y-%m-%d')
        r = requests.get(self.url)
        weather = json.load(StringIO(r.content))
        for data in weather.get('forecasts'):
            if tomorrow == data.get('date'):
                message = []
                message.append(tomorrow)
                message.append(u'forecasts:' + data.get('image').get('title'))
                temperature_max = data.get('temperature').get('max')
                if temperature_max and temperature_max.get('celsius'):
                    message.append(u'max celsius:' + temperature_max.get('celsius'))
                temperature_min = data.get('temperature').get('min')
                if temperature_min and temperature_min.get('celsius'):
                    message.append(u'min celsius:' + temperature_min.get('celsius'))
                return " ".join(message)

    def get_weather_day_after_tomorrow(self):
        # TODO timedelta 以外は同じなのでまとめる
        today = datetime.now(pytz.timezone('Asia/Tokyo'))
        days = timedelta(days = 2)
        tomorrow = (today + days).strftime('%Y-%m-%d')
        r = requests.get(self.url)
        weather = json.load(StringIO(r.content))
        for data in weather.get('forecasts'):
            if tomorrow == data.get('date'):
                message = []
                message.append(tomorrow)
                message.append(u'forecasts:' + data.get('image').get('title'))
                temperature_max = data.get('temperature').get('max')
                if temperature_max and temperature_max.get('celsius'):
                    message.append(u'max celsius:' + temperature_max.get('celsius'))
                temperature_min = data.get('temperature').get('min')
                if temperature_min and temperature_min.get('celsius'):
                    message.append(u'min celsius:' + temperature_min.get('celsius'))
                return " ".join(message)
