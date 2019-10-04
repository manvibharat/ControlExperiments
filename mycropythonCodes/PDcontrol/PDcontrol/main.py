#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()


motor = Motor(Port.B)

desired_motor_angle=180




kp=.1
kd=2
angle=[]
t=[]
motor.reset_angle(0)
watch = StopWatch()
seconds = watch.time()/1000

while seconds < 10:
    seconds = watch.time()/1000
    t.append(seconds)
    error=desired_motor_angle-motor.angle()
    duty_cycle = kp * error * 19 
    motor.dc(duty_cycle)
    angle.append(motor.angle())
    errortime=seconds
       

print('t =',t,';')
print('angle =',angle,';')
