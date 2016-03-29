#!/usr/bin/env python

import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('sonos_weather.cfg')

api_key = config.get('weather', 'api_key')

print api_key




