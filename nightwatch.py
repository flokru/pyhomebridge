#!/usr/bin/env python3

import pendulum

now = pendulum.now()
night_start = pendulum.now().start_of('day').add(hours=23)
night_end = pendulum.now().start_of('day').add(hours=5)

if now <= night_end or now >= night_start:
    print("true")
else:
    print("false")