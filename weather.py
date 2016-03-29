#!/usr/bin/env python

import pyowm
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('sonos_weather.cfg')

api_key = config.get('weather', 'api_key')
location = "Lafayette, CO, USA"

owm = pyowm.OWM(api_key)

observation = owm.weather_at_place(location)
weather = observation.get_weather()

temperature_fahrenheit = weather.get_temperature('fahrenheit')
