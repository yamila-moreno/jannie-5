jannie-5
========
Sensor-armed glove driven drone, for VII Piweek. You can read more and watch a video [here](http://moduslaborandi.net/vii-piweek-jannie-5/).

This integration uses a slightly trimmed version of (https://github.com/venthur/python-ardrone)

Hardware installation
---------------------

You will need:
- Parrot ARDrone 2.0
- Arduino Yún and power source (e.g. a 5V USB battery or an AC plug)
- [Triple Axis Accelerometer Breakout MMA8452Q](https://www.sparkfun.com/products/12756)
- [Force Sensitive Resistor](https://www.sparkfun.com/products/9375)
- [Flex Sensor](https://www.sparkfun.com/products/8606)
- 2 x 330 Ohm resistors
- 2 x 10 KOhm resistors
- A breadboard and wire
- A glove you can sew the sensors into

The Fritzing schematic of the circuit can be found inside the `docs` folder of the repo.

![alt text](https://github.com/yamila-moreno/jannie-5/blob/master/docs/schematic_bb.png "Fritzing schematic")

The sensors are meant to be sewed into the glove: for example, the Accelerometer to the palm of the hand, the Force Sensitive Resistor to the thumb and the Flex sensor the a finger. You will need long wires (for "maker" bonus points use conductive thread).

Software installation
---------------------

1. Clone this repo in order to retrieve the latest version of the files
2. Compile and upload the sketch `Ardruino.ino` to the Yún. You will need Arduino IDE 1.5.8+ and the [SFEMMA8452Q library](https://github.com/sparkfun/MMA8452_Accelerometer/tree/master/Firmware/libraries/SFE_MMA8452Q)
3. Copy the `src` folder to the `/root` folder of the Yún's Linino and install the python dependencies:

   ```
   opkg update
   opkg install distribute
   opkg install python-openssl
   easy_install pip
   pip install -r requirements.txt
   ```
4. Configure the Yun to automatically connect to the ARDrone WiFi (no encription!)
5. Test the library. If you grab the `libardrone-example.py` from the `examples` folder and put in into the same `src` directory, you will be able to test the library directly from the command line:

   ```
   python libardone-example.py
   ```
   Make sure the ARDrone is on and the Yún connected to the ARDrone WiFi
6. Start the API server on a console of the Yún or, even better, create a init script that runs the server headless:
       
   ```
   python ardrone_server.py
   ```
7. Test the API with the example:

   ```
   python bottle-example.py
   ```
8. If everything works, hold the glove and try to fly the ARDrone with it. Hints:
       - Push the Force Sensitive Resistor to take off / land
       - Flex the Flex Sensor to enable the Accelerometer control. Release it to hover.
       - Tilt the Accelerometer to move the drone in the horizontal plane

9. Enjoy :-)
