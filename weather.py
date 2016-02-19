# -*- coding: utf-8 -*-
import click
from states_store import StateStore
from weather_store import WeatherStore

states = StateStore()
#print states.get_citys_by_state(u'千葉県')
#print states.get_city_id_by_name(u'銚子')

city = states.get_city_id_by_name(u'東京')
weatherStore = WeatherStore(city=city)

@click.command()
@click.option('--today', '-t', 'scope', flag_value='today', help='Show the today weather')
@click.option('--tomorrow', '-tt', 'scope', flag_value='tomorrow', help='Show the tomorrow weather')
@click.option('--aftertomorrow', '-ttt', 'scope', flag_value='aftertomorrow', help='Show the day after tomorrow weather')
def weather(scope):
    empty_messagy = 'Nothing forecasts'
    if scope == 'tomorrow':
        print weatherStore.get_weather_tomorrow() or empty_messagy
    elif scope == 'aftertomorrow':
        print weatherStore.get_weather_day_after_tomorrow() or empty_messagy
    else:
        print weatherStore.get_weather_today() or empty_messagy

if __name__ == '__main__':
    weather()
