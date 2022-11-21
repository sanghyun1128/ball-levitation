import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, trigPinNum, echoPinNum):
        self.trigPinNum = trigPinNum
        self.echoPinNum = echoPinNum
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigPinNum, GPIO.OUT)
        GPIO.setup(self.echoPinNum, GPIO.IN)
        
    def getDistance(self):
        GPIO.output(self.trigPinNum, 0)
        time.sleep(0.000002)

        GPIO.output(self.trigPinNum, 1)
        time.sleep(0.00001)
        GPIO.output(self.trigPinNum, 0)

        while GPIO.input(self.echoPinNum) == 0:
            a = 0
        time1 = time.time()
        while GPIO.input(self.echoPinNum) == 1:
            a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100
    
    def destroy():
        GPIO.cleanup()

