from fan import Fan
from ultrasonic import Ultrasonic
import RPi.GPIO as GPIO
GPIO.cleanup()

fan = Fan(23)
ultrasonic = Ultrasonic(17, 18)

fan.setup()
ultrasonic.setup()

desireDistance = 20

currentSpeed = 50
fan.setFanSpeed(currentSpeed)

try:
    while(1):
        fan.pwmOnFan10ms()
        distance = ultrasonic.getDistance()
        if (distance < desireDistance):
            currentSpeed -= 5
            fan.setFanSpeed(currentSpeed)
        else :
            currentSpeed += 5
            fan.setFanSpeed(currentSpeed)
except KeyboardInterrupt:
    fan.destory()
    ultrasonic.destroy()