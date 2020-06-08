#!/usr/bin/python3

from gpiozero import LED
import sys
import time

lookup = {
    'back1': 14,
    'back2': 15,
    'back3': 18,
    'back4': 23,
    'front1': 2,
    'front2': 3,
    'front3': 4,
    'front4': 17 }


if __name__ == '__main__':
    station = lookup[sys.argv[1]]
    duration = 60 * float(sys.argv[2])
    startWatering = LED(station)
    time.sleep(int(duration))
