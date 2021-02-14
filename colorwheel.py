#!/usr/bin/env python3

from phue import Bridge
import random

b = Bridge('192.168.0.11')
b.connect()
b.lights
light = b.lights_by_name['Wohnzimmer Sideboard Stehlampe']
light.transitiontime = 5
light.on = True
light.xy = (random.random(), random.random())
light.saturation = int(random.random() * 255.0)
light.brightness = 255