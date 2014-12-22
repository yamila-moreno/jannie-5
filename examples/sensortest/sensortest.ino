#include <Wire.h> // Must include Wire library for I2C
#include <SFE_MMA8452Q.h> // Includes the SFE_MMA8452Q library

int flexiPin = A0;
int flexiValue;
String flexiValues = "";

int pressPin = A1;
int pressValue;
int degreesValue;
String pressValues = "";

MMA8452Q accel; // Default MMA8452Q object create. (Address = 0x1D)
float xAccel;
float yAccel;
float zAccel;
String accelerationValues = "";
float cxAccel;
float cyAccel;
float czAccel;
String calculatedValues = "";

void setup(){
    Serial.begin(9600);
    Serial.println("Initializing accelerometer: ");
    accel.init(); // Default init: +/-2g and 800Hz ODR
    Serial.println("Done!");
}

void loop(){
    // TEST
    //letters = letters + "hola" + "y adios";
    //letters = letters + "b" + "c";
    //letters = letters + 1234;

    // FLEXOMETER
    flexiValue = analogRead(flexiPin);
    degreesValue = map(flexiValue, 250, 200, 0, 90);
    flexiValues = flexiValues + "flexiValue: " + flexiValue + " / degreesValues: " + degreesValue;
    Serial.println(flexiValues);
    flexiValues = "";
    // PRESSURE
    pressValue = analogRead(pressPin);
    pressValues = pressValues + "pressValue: " + pressValue;
    Serial.println(pressValues);
    pressValues = "";
    // ACCELEROMETER
    accel.read();
    xAccel = accel.x;
    yAccel = accel.y;
    zAccel = accel.z;
    accelerationValues = accelerationValues + "accelerationValues: " + xAccel + " / " + yAccel + " / " + zAccel;
    Serial.println(accelerationValues);
    accelerationValues = "";
    cxAccel = accel.cx;
    cyAccel = accel.cy;
    czAccel = accel.cz;
    calculatedValues = calculatedValues + "calculatedValues: " + cxAccel + " / " + cyAccel + " / " + czAccel;
    Serial.println(calculatedValues);
    calculatedValues = "";
    delay(500);
}

