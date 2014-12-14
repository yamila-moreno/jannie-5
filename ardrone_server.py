from bottle import route, run, template
import libardrone

class ArDrone(object):
    def __init__(self):
        self.a = 'this is an a'
        self.b = 'this is a b'

    def do_a(self):
        return self.a

    def do_b(self):
        return self.b

drone = None

@route('/takeoff')
def a():
    if not drone:
        start_drone()
    res = drone.do_a()
    return template('<b>Do a</b>! : {{res}}', res=res)

@route('/land')
def b():
    if not drone:
        start_drone()
    res = drone.do_b()
    return template('<b>Do b</b>! : {{res}}', res=res)

def start_drone():
    global drone
    drone = ArDrone()

run(host='0.0.0.0', port=8080)
