from bottle import route, run, template
import libardrone

drone = None
speed = 0.1

#TODO: review ARDrone.move() method
# maybe useful instead of the wapped methods

@route('/takeoff')
def takeoff():
    if not drone:
        start_drone()
    drone.takeoff()
    drone.hover()

@route('/land')
def land():
    if not drone:
        start_drone()
    drone.land()

@route('/hover')
def hover():
    if not drone:
        start_drone()
    drone.hover()

@route('/trim')
def trim():
    if not drone:
        start_drone()
    drone.trim()

@route('/accelerate')
def accelerate():
    if not drone:
        start_drone()
    global speed
    if speed < 1:
        speed += 0.1
    drone.set_speed(speed)

@route('/slow/down')
def slow_down():
    if not drone:
        start_drone()
    global speed
    if speed > 0:
        speed -= 0.1
    drone.set_speed(speed)

@route('/shutdown')
def trim():
    if not drone:
        start_drone()
    drone.halt()

@route('/go/left')
def go_left():
    if not drone:
        start_drone()
    drone.move_left()

@route('/go/right')
def go_right():
    if not drone:
        start_drone()
    drone.move_right()

@route('/go/up')
def go_up():
    if not drone:
        start_drone()
    drone.move_up()

@route('/go/down')
def go_down():
    if not drone:
        start_drone()
    drone.move_down()

@route('/go/forward')
def go_forward():
    if not drone:
        start_drone()
    drone.move_forward()

@route('/go/backward')
def go_backward():
    if not drone:
        start_drone()
    drone.move_backward()

@route('/spin/left')
def spin_left():
    if not drone:
        start_drone()
    drone.turn_left()

@route('/spin/right')
def spin_right():
    if not drone:
        start_drone()
    drone.turn_right()

def start_drone():
    global drone
    drone = ArDrone()

def keep_alive():
    drone.commwdg()

run(host='0.0.0.0', port=8080)
