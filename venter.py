#!/usr/bin/env python3

from phue import Bridge
import denonavr
import time
import logging

this_state_since = 0
switch_lag_rounds = 10
tick_time = 60
state_previous = ''

def configure_logger(verbosity, log_file=None):
    formatter = logging.Formatter('%(asctime)s | %(levelname)s |'
                              ' %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    if verbosity >= 1:
        console.setLevel(logging.DEBUG)
    else:
        console.setLevel(logging.INFO)
    logger = logging.getLogger('VenterLogger')
    logger.addHandler(console)
    if log_file is not None:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        if verbosity >= 1:
            fh.setLevel(logging.DEBUG)
        else:
            fh.setLevel(logging.INFO)
        logger.addHandler(fh)
    # logger.propagate = False
    if verbosity >= 1:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


def get_logger():
    logger = logging.getLogger('VenterLogger')
    return logger


d = denonavr.DenonAVR("192.168.0.12", "Denon")

b = Bridge('192.168.0.11')
b.connect()
b.lights
box = b.lights_by_name['Lüftung TV-Bank']

configure_logger(1)
logger = get_logger()

while True:
    d.update()
    if d.power != state_previous:
        this_state_since = 0
        logger.debug(f'State change from "{state_previous}" to "{d.power}"')
        state_previous = d.power
    else:
        this_state_since += tick_time
    if this_state_since == (switch_lag_rounds + 1) * tick_time:
        if state_previous == 'ON':
            logger.debug(f'Switching on after lag of '
                         f'{switch_lag_rounds * tick_time} s')
            box.on = True
        if state_previous == 'OFF':
            logger.debug(f'Switching off after lag of '
                         f'{switch_lag_rounds * tick_time} s')
            box.on = False
    time.sleep(tick_time)
