import RPi.GPIO as GPIO
import time

class Fan:
    def __init__(self, fanPinNum):
        self.fanPinNum = fanPinNum
        self.fanSpeed = 0
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.fanPinNum, GPIO.OUT)
        
    def setFanSpeed(self, fanSpeed):
        self.fanSpeed = fanSpeed
        
    def pwmOnFan10ms(self):
        for i in range(self.fanSpeed):
            GPIO.output(self.fanPinNum, True)
            time.sleep(0.0001)
        for j in range(100-self.fanSpeed):
            GPIO.output(self.fanPinNum, False)
            time.sleep(0.0001)
                
    def destory():
        GPIO.cleanup()