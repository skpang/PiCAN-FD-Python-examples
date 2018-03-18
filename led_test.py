import RPi.GPIO as GPIO
import time
led = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)

for m in range(0,16):
    
     print(m)
     time.sleep(0.02)
time.sleep(0.05)
GPIO.output(led,False)
