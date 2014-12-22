# -*- coding: utf-8 -*-

from time import sleep
import libardrone

def with_lib():
    d = libardrone.ARDrone()
    d.takeoff()
    d.hover()
    sleep(5)
    d.move_forward()
    sleep(3)
    d.land()
    d.halt()

if __name__ == "__main__":
    with_lib()
