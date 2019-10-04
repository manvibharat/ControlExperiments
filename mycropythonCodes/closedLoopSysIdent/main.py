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
brick.sound.beep()                      #Just to indicate

motor = Motor(Port.B)
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

from math import sin

motor = Motor(Port.B)

f=8
amplitude = 180
t=[]
angle=[]
desd=[]

watch = StopWatch()
seconds = watch.time()/1000
motor.reset_angle(0)

    

while seconds < 10:
    seconds = watch.time()/1000
    t.append(seconds)
    
    
    desired_motor_angle = sin(2*3.14*seconds*f)*amplitude
    desd.append(desired_motor_angle)
    error=desired_motor_angle-motor.angle()
    duty_cycle = kp * error * 19 
    motor.dc(duty_cycle)
    angle.append(motor.angle())
    
    wait(10)

print('t =',t)
print('angle =',angle)
print('desd =',desd)
print('f =',f)

