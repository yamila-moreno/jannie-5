# -*- coding: utf-8 -*-

from time import sleep
import subprocess

def invoke_rest_api(cmd):
    url = 'http://localhost:8080/{}'.format(cmd)
    subprocess.call(['curl', url])

if __name__ == "__main__":
    # start
    invoke_rest_api('start')
    invoke_rest_api('takeoff')
    sleep(5)
    # go forward
    invoke_rest_api('go_forward')
    sleep(2)
    invoke_rest_api('hover')
    sleep(5)
    # go backward
    invoke_rest_api('go_backward')
    sleep(2)
    invoke_rest_api('hover')
    # land
    invoke_rest_api('land')
    invoke_rest_api('stop')
