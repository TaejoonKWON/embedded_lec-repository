import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)

try:
    while True:
       #LED1 점등 및 소등
        GPIO.output(37,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(37,GPIO.LOW)
        time.sleep(0.5)

        #LED2 점등 및 소등
        GPIO.output(36,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(36,GPIO.LOW)
        time.sleep(0.5)

        #LED4 점등 및 소등
        GPIO.output(40,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(40,GPIO.LOW)
        time.sleep(0.5)

        #LED3 점등 및 소등
        GPIO.output(38,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(38,GPIO.LOW)
        time.sleep(0.5)

except:
    #cleanup 함수로 핀 reset
    GPIO.cleanup()