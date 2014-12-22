from bottle import route, run
import libardrone
from time import sleep

drone = None
speed = 0.1

@route('/start')
def start():
    global drone
    drone = libardrone.ARDrone()

@route('/takeoff')
def takeoff():
    drone.takeoff()
    drone.hover()

@route('/land')
def land():
    drone.land()
    sleep(4)

@route('/stop')
def stop():
    drone.halt()

@route('/hover')
def hover():
    drone.hover()

@route('/trim')
def trim():
    drone.trim()

@route('/accelerate')
def accelerate():
    global speed
    if speed < 1:
        speed += 0.1
    drone.set_speed(speed)

@route('/slow_down')
def slow_down():
    global speed
    if speed > 0:
        speed -= 0.1
    drone.set_speed(speed)

@route('/go_left')
def go_left():
    drone.move_left()

@route('/go_right')
def go_right():
    drone.move_right()

@route('/go_up')
def go_up():
    drone.move_up()

@route('/go_down')
def go_down():
    drone.move_down()

@route('/go_forward')
def go_forward():
    drone.move_forward()

@route('/go_backward')
def go_backward():
    drone.move_backward()

@route('/spin_left')
def spin_left():
    drone.turn_left()

@route('/spin_right')
def spin_right():
    drone.turn_right()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
