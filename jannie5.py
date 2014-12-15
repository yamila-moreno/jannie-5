# -*- coding: utf-8 -*-

import libardrone
import sys

if __name__ == "__main__":

    drone = libardrone.ARDrone()

    try:
        while 1:
            try:
                print('Enter a single char')
                cmd = sys.stdin.read(1)
                c = c.lower()

                if c == 't':
                    drone.takeoff()
                    drone.hover()
                elif c == 'h':
                    drone.move_left()
                    drone.hover()
                elif c == 'l':
                    drone.move_right()
                    drone.hover()
                elif c == 'j':
                    drone.move_forward()
                    drone.hover()
                elif c == 'k':
                    drone.move_backward()
                    drone.hover()
                elif c == 'a':
                    drone.land()
                else:
                    drone.hover()
            except IOError:
                pass
    finally:
        drone.halt()
