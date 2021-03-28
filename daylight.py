#!/usr/bin/env python3

import sys
import pendulum
from astral.geocoder import database, lookup
from astral.sun import sun


def on():
    pass


def off():
    pass


def status():
    now = pendulum.now()
    night_end = pendulum.now().start_of('day').add(hours=5)
    location = lookup("Berlin", database())
    s = sun(location.observer, date=now)
    evening_start = pendulum.now().start_of('day').add(hours=18)
    # if now >= night_end and now <= s['dusk']:
    if now >= night_end and now <= evening_start:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('call with --on --off --status')
    elif sys.argv[1] == '--on':
        on()
    elif sys.argv[1] == '--off':
        off()
    elif sys.argv[1] == '--status':
        status()
    else:
        print('call with --on --off --status')
