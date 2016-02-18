# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as xml
import json
from pprint import pprint

class StateStore():

    def __init__(self, debug = False):
        self.debug = debug
        self.states = self.load_states()

    def load_states(self):
        """
            Get Japan States and Citys.
            returns [
                state: {
                    id,
                    label,
                },
                citys: [{
                    id,
                    label,
                }]
            ]
        """
        # FIXME キャッシュする
        r = requests.get('http://weather.livedoor.com/forecast/rss/primary_area.xml')
        area = xml.fromstring(r.content)

        # FIXME キャッシュする
        states_file = open('./state_code.json', mode='r')
        states = json.load(states_file)
        dict_states = {}
        for state in states['results']['bindings']:
            dict_states[state['label_ja'].get('value')] = int(state['area_code'].get('value'))

        states = []
        for data in area.findall(".//pref"):
            state = {
                'state': {
                    'id' : dict_states.get(data.get('title')),
                    'label': data.get('title'),
                },
                'citys': [],
            }
            for city in data.findall("city"):
                state['citys'].append({
                    'id': city.get('id'),
                    'label': city.get('title'),
                })

            states.append(state)

        for state in states:
            if self.debug:
                print "都道府県：", state['state'].get('label'), state['state'].get('id')
            for city in state['citys']:
                if self.debug:
                    print "都市：", city.get('label'), city.get('id')
        return states

    def get_city_id_by_name(self, name):
        for state in self.states:
            for city in state.get('citys'):
                if city.get('label') == name:
                    return city.get('id')

    def get_citys_by_state(self, name):
        for state in self.states:
            if state['state'].get('label') == name:
                return ','.join([ city.get('label') for city in state['citys']])
