# -*- coding: utf-8 -*-
import click
from states_store import StateStore
from weather_store import WeatherStore

states_store = StateStore()

@click.group()
def run():
    pass

@run.command()
@click.option('--state', '-s', default=None, help='Show cities list from state.')
def cities(state):
    if state is None:
        print 'Usage: cities --state [state name]'
    else:
        print states_store.get_cities_by_state(state)


@run.command()
@click.option('--today', '-t', 'scope', flag_value='today', help='Show the today weather.')
@click.option('--tomorrow', '-tt', 'scope', flag_value='tomorrow', help='Show the tomorrow weather.')
@click.option('--aftertomorrow', '-ttt', 'scope', flag_value='aftertomorrow', help='Show the day after tomorrow weather.')
@click.option('--city', '-c', default=u'東京', help='The city name to see the weather.')
def forecasts(scope, city):
    empty_messagy = 'Nothing forecasts'

    city_id = states_store.get_city_id_by_name(city)
    weatherStore = WeatherStore(city=city_id)

    if scope == 'tomorrow':
        print weatherStore.get_weather_tomorrow() or empty_messagy
    elif scope == 'aftertomorrow':
        print weatherStore.get_weather_day_after_tomorrow() or empty_messagy
    else:
        print weatherStore.get_weather_today() or empty_messagy

if __name__ == '__main__':
    run()
