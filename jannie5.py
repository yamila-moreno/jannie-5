# -*- coding: utf-8 -*-

import ardrone_server as ar
from time import sleep

if __name__ == "__main__":
    # start
    ar.start()
    ar.takeoff()
    sleep(5)
    # go forward
    ar.go_forward()
    sleep(2)
    ar.hover()
    sleep(5)
    # go backward
    ar.go_backward()
    sleep(2)
    ar.hover()
    # land
    ar.land()
    ar.stop()
