jannie-5
========
Arduino Yun driven drone, for VII Piweek

Requirements:
- arduino yún
- python2.7
- virtualenv
- bottle
- parrot ardrone


Process
=======
(this is not a proper documentation, only notes during the process)

- arduino is connected to sensors
- using the Process.h library arduino can invoke commands in linux
- in the linux side, we have a bottle server (APIlike app to be called from arduino)
- with an init.d script to start at Yun boot
- this bottle server connects to the libardrone library to send UDP messages to the drone

Note::

    every command starts and doesn't end if no other command is recieved. For instance, if you send "go up" comand, it will raise until changing the vertical speed; so, you would need to go_vertical(1) (means go up at speed 1) and then go_vertical(0) to stop raising.
