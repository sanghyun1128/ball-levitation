from fan import Fan
from ultrasonic import Ultrasonic
from pid import PID_Control
import RPi.GPIO as GPIO
GPIO.cleanup()

fan = Fan(23)
ultrasonicForPid = Ultrasonic(17, 18)
ultrasonicForDistance = Ultrasonic(20, 21)
pid = PID_Control(0.1, 0, 100, 4, 1.2, 2.5)

fan.setup()
ultrasonicForDistance.setup()
ultrasonicForPid.setup()

try:
    while(1):
        currdistance = ultrasonicForPid.getDistance()
        desireDistance = 50 - int(ultrasonicForDistance.getDistance())
        if desireDistance < 0:
            desireDistance = 25
        speed = pid.calc(currdistance, desireDistance)
        fan.setFanSpeed(speed)
        print("Desire : " + str(desireDistance))
        print("Distance : " + str(currdistance) + " / " + "Speed : " + str(fan.getSpeed()))
        fan.pwmOn100ms()
except KeyboardInterrupt:
    fan.destory()
    ultrasonicForPid.destroy()
    ultrasonicForDistance.destroy()