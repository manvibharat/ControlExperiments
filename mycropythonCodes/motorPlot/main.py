#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from math import sin


# Write your program here
brick.sound.beep()
# This code runs on Lego Ev3 not on your computer
# The code send sinewave as an input and collect angular position values from wheel encoder



motor = Motor(Port.B)               # Select the motor port
amplitude = float(100)              # Amplitude of the duty cycle which is in percentage
f=.7                          # Choose input frequency
t=[]                                # intialize list to store time                
ang_pos=[]
speed=[]                          # Intialize list to store angular position from wheel encoder
watch = StopWatch()                 # Using inbuild timer to keep track of time
seconds = watch.time()/1000         # Converting into seconds
motor.reset_angle(0)                # Initialize motor angular position to '0'
inp=[]
while seconds < 5 :                # Runs for ten seconds
    
    seconds = watch.time()/1000     # Time in seconds
    t.append(seconds)               # Store time in 't'
    
   
    duty_cycle = sin(2*3.14*seconds*f)*amplitude  # Calculate dutycycle
    inp.append(duty_cycle)
    
    motor.dc(duty_cycle)                          # Giving dutycycle as an input
    ang_pos.append(motor.angle())                 # Storing angular position in angle
    speed.append(motor.speed())
    
    wait(10)                                      # Choosing sampling frequency approximately 100Hz, Because wait takes in 10ms delay which is 1/10ms=100Hz

#-----------------------------------------------
# Print all values on to terminal
print('volta =',brick.battery.voltage())
print('t =',t)
print('ang_pos =',ang_pos)
print('f =',f)
print('speed',speed)
print('input',inp)