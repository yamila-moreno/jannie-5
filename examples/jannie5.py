# -*- coding: utf-8 -*-

from time import sleep
import subprocess

def invoke_rest_api(cmd):
    url = 'http://localhost:8080/{}'.format(cmd)
    subprocess.call(['curl', url])

def with_api():
    # start
    invoke_rest_api('start')
    invoke_rest_api('takeoff')
    sleep(3)
    # go forward
    invoke_rest_api('go_forward')
    sleep(4)
    # go backward
    invoke_rest_api('go_backward')
    sleep(4)
    # land
    invoke_rest_api('land')
    invoke_rest_api('stop')

def with_lib():
    import libardrone
    d = libardrone.ARDrone()
    d.takeoff()
    d.hover()
    sleep(5)
    d.move_forward()
    sleep(3)
    d.land()
    d.halt()
    
if __name__ == "__main__":
    with_api()
    #with_lib()
