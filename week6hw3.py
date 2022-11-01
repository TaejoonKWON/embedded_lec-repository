import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

def front():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    print("SW1 Click")

def rear():
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    print("SW4 Click")

def right():
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(100)
    print("SW3 Click")

def left():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(100)
    print("SW2 Click")

try:
    while True:
        if GPIO.input(SW1) == 1:
            front()
        elif GPIO.input(SW2) == 1:
            left()
        elif GPIO.input(SW3) == 1:
            right()
        elif GPIO.input(SW4) == 1:
            rear()
        else:
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()