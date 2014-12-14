jannie-5
========

Arm driven drone, for VII Piweek

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
