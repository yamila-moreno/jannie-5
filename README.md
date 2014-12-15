jannie-5
========
Arduino Yún driven drone, for VII Piweek

Requirements:
- Arduino yún
- Python2.7
- Virtualenv
- Bottle
- Parrot ardrone


Process
=======
(this is not a proper documentation, only notes during the process)

- Arduino is connected to sensors
- Using the Process.h library arduino can invoke commands in linux
- On the linux side, we have a bottle server (API-like app to be called from arduino)
- With an init.d script to start at Yun boot
- This bottle server connects to the libardrone library to send UDP messages to the drone

Note::

    every command starts and doesn't end if no other command is recieved. For instance, if you send "go up" comand, it will raise until changing the vertical speed; so, you would need to go_vertical(1) (means go up at speed 1) and then go_vertical(0) to stop raising.
