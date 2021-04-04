#!/usr/bin/env python3

from phue import Bridge
import denonavr
import time

this_state_since = 0
switch_lag_rounds = 3
tick_time = 10
state_previous = ''

d = denonavr.DenonAVR("192.168.0.12", "Denon")

b = Bridge('192.168.0.11')
b.connect()
b.lights
box = b.lights_by_name['Steckdose Weihnachtsbaum']

while True:
    d.update()
    if d.power != state_previous:
        this_state_since = 0
        state_previous = d.power
        print('state change')
    else:
        this_state_since += tick_time
    if this_state_since == (switch_lag_rounds + 1) * tick_time:
        if state_previous == 'ON':
            print(f'switching on after lag of '
                  f'{switch_lag_rounds * tick_time}')
            box.on = True
        if state_previous == 'OFF':
            print(f'switching off after lag of '
                  f'{switch_lag_rounds * tick_time}')
            box.on = False
    time.sleep(tick_time)
