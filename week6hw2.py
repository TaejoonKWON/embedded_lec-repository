import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
BUZZER = 12
list_sw = [SW1, SW2, SW3, SW4]
list_doremifa = [262, 294, 330, 349]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(list_sw[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,261)

try:
    while True:
        for i in range(4):
            if GPIO.input(list_sw[i]) == 1:
                p.start(50)
                p.ChangeFrequency(list_doremifa[i])
                time.sleep(0.1)
            else:
                p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()