#!/usr/bin/env python3

from phue import Bridge
import random
import sys


def wheel():
    b = Bridge('192.168.0.11')
    b.connect()
    b.lights
    light = b.lights_by_name['Wohnzimmer Sideboard Stehlampe']
    light.transitiontime = 5
    light.on = True
    color = (random.random(), random.random())
    print(f'Setting to color: {color}')
    light.xy = color
    light.saturation = int(random.random() * 255.0)
    light.brightness = 255


def off():
    b = Bridge('192.168.0.11')
    b.connect()
    b.lights
    light = b.lights_by_name['Wohnzimmer Sideboard Stehlampe']
    light.on = False


def status():
    b = Bridge('192.168.0.11')
    b.connect()
    b.lights
    light = b.lights_by_name['Wohnzimmer Sideboard Stehlampe']
    if light.on:
        print('true')
    else:
        print('false')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('call with --on --off --status')
    elif sys.argv[1] == '--on':
        wheel()
    elif sys.argv[1] == '--off':
        off()
    elif sys.argv[1] == '--status':
        status()
    else:
        print('call with --on --off --status')

