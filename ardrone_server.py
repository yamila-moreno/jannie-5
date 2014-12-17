from bottle import route, run, template
import libardrone

drone = None
speed = 0.1

#TODO: review ARDrone.move() method
# maybe is useful a decorator instead of the condition

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

@route('/slow/down')
def slow_down():
    global speed
    if speed > 0:
        speed -= 0.1
    drone.set_speed(speed)

@route('/go/left')
def go_left():
    drone.move_left()

@route('/go/right')
def go_right():
    drone.move_right()

@route('/go/up')
def go_up():
    drone.move_up()

@route('/go/down')
def go_down():
    drone.move_down()

@route('/go/forward')
def go_forward():
    drone.move_forward()

@route('/go/backward')
def go_backward():
    drone.move_backward()

@route('/spin/left')
def spin_left():
    drone.turn_left()

@route('/spin/right')
def spin_right():
    drone.turn_right()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
