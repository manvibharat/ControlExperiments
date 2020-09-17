#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from math import pi
# Write your program here
brick.sound.beep()


motor = Motor(Port.B)

desired_motor_angle=360
eta=0.5
K=110*4*pi
sigma=4*pi
wn=sigma/(2*eta)
kp=(wn*wn)/K


angle=[]
t=[]
motor.reset_angle(0)
watch = StopWatch()
seconds = watch.time()/1000

while seconds < 5:
    seconds = watch.time()/1000
    t.append(seconds)
    error=desired_motor_angle-motor.angle()
    duty_cycle = kp * error * 20
    motor.dc(duty_cycle)
    angle.append(motor.angle())
    
       

print('t =',t)
print('angle =',angle)
