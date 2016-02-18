# -*- coding: utf-8 -*-

from states_store import StateStore
from weather_store import WeatherStore

states = StateStore()
#print states.get_citys_by_state(u'千葉県')
#print states.get_city_id_by_name(u'銚子')

city = states.get_city_id_by_name(u'東京')
weather = WeatherStore(city=city)
weather.get_weather_description()

print weather.get_weather_today()
print weather.get_weather_tomorrow()
print weather.get_weather_day_after_tomorrow()
