import RPi.GPIO as GPIO
import time

class Fan:
    def __init__(self, fanPinNum):
        self.fanPinNum = fanPinNum
        self.fanSpeed = 0
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.fanPinNum, GPIO.OUT)
        
    def getSpeed(self):
        return self.fanSpeed
    def setFanSpeed(self, fanSpeed):
        self.fanSpeed = int(fanSpeed)
    
    def addFanSpeed(self, num):
        self.fanSpeed += num
        if self.fanSpeed > 100:
            self.fanSpeed = 100
    
    def minusFanSpeed(self, num):
        self.fanSpeed -= num
        if self.fanSpeed < 0:
            self.fanSpeed = 0
        
    def pwmOnFan100ms(self):
        GPIO.output(self.fanPinNum, True)
        for i in range(self.fanSpeed):
            time.sleep(0.001)
        GPIO.output(self.fanPinNum, False)
        for j in range(100-self.fanSpeed):
            time.sleep(0.001)
                
    def destory(self):
        GPIO.cleanup()