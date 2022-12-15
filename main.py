from fan import Fan
from ultrasonic import Ultrasonic
from pid import PID_Control
import RPi.GPIO as GPIO
GPIO.cleanup()

fan = Fan(23)
ultrasonic = Ultrasonic(17, 18)
pid = PID_Control(0.1, 0, 100, 1, 1, 1)

fan.setup()
ultrasonic.setup()

desireDistance = 20

prevErr = 20
try:
    while(1):
        currdistance = ultrasonic.getDistance()
        fan.setFanSpeed(pid.calc(currdistance, desireDistance))
        print("Distance : " + str(currdistance) + " / " + "Speed : " + str(fan.getSpeed()))
        fan.pwmOnFan100ms()
except KeyboardInterrupt:
    fan.destory()
    ultrasonic.destroy()