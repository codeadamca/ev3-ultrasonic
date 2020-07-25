#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Initialize EV3 touch sensor and motors
motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
ultrasonicA = UltrasonicSensor(Port.S1)

# Create a loop to react to distance
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        motorLeft.stop()
        motorRight.stop()
        break

    # React to the distance
    if ultrasonicA.distance() < 100:
        motorLeft.stop()
        motorRight.stop()

    else:
        motorLeft.dc(50)
        motorRight.dc(50)

    # Uncomment to display the current distance reading
    print("Distance: ", ultrasonicA.distance())

    wait(1000)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
