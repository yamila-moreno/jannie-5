#include <Process.h>
#include <Wire.h> // Must include Wire library for I2C
#include <SFE_MMA8452Q.h> // Includes the SFE_MMA8452Q library

String url;
String cmd;

int pressPin = A1;
int pressValue;

int flexiPin = A0;
float flexiValue;
float degreesValue;

MMA8452Q accel; // Default MMA8452Q object create. (Address = 0x1D)

bool droneStarted = false;

void sendDroneAction(String action)
{
    Process p;
    url = "http://localhost:8080/" + action;
    cmd = "curl " + url;
    p.runShellCommand(cmd);
}

void setup()
{
    Serial.println("Initializing accelerometer: ");
    accel.init(); // Default init: +/-2g and 800Hz ODR
    Serial.println("Done!");
    Bridge.begin();
    Serial.begin(9600);
}

void loop()
{
    pressValue = analogRead(pressPin);
    Serial.print("pressValue: ");
    Serial.println(pressValue);

    if(pressValue > 400)
    {
        if(!droneStarted)
        {
            Serial.println("Take care, we are taking off");
            Serial.println("****************************");
            //sendDroneAction("start");
            //sendDroneAction("takeoff");
            droneStarted = true;
        }
        else
        {
            Serial.println("Fasten your belt, we are landing");
            Serial.println("****************************");
            //sendDroneAction("land");
            //sendDroneAction("stop");
            droneStarted = false;
        }
    }
    else
    {
        if(droneStarted)
        {
            flexiValue = analogRead(flexiPin);
            degreesValue = map(flexiValue, 250, 200, 0, 90); //from 0 to 90
            Serial.print("flexed degreesValue: ");
            Serial.println(degreesValue);
            delay(500);
            if(degreesValue > 100)
            {
                Serial.println("Reading accelerometer: ");

                accel.read();
                //Serial.print("accelerationValues: ");
                //Serial.print(accel.x);
                //Serial.print(" / ");
                //Serial.print(accel.y);
                //Serial.print(" / ");
                //Serial.println(accel.z);
                Serial.print("calculatedValues: ");
                Serial.print(accel.cx);
                Serial.print(" / ");
                Serial.print(accel.cy);
                Serial.print(" / ");
                Serial.println(accel.cz);
            }
            else
            {
                Serial.println("Order hover");
                delay(1000);
                //sendDroneAction("hover");
            }
        }
    }
    delay(1000);
}
