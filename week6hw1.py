import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
sw1Value = 0
sw2Value = 0
sw3Value = 0
sw4Value = 0
sw1Count = 0
sw2Count = 0
sw3Count = 0
sw4Count = 0

list_switch = [SW1, SW2, SW3, SW4]
list_value = [sw1Value, sw2Value, sw3Value, sw4Value]
list_count = [sw1Count, sw2Count, sw3Count, sw4Count]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(list_switch[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(4):
            if GPIO.input(list_switch[i]) == 1:
                list_count[i] = list_count[i] + 1
                print("('SW" + str(i+1) + " Click', " + str(list_count[i]) + ")")
                time.sleep(0.5)
                if GPIO.input(list_switch[i]) == 0:
                    break

except KeyboardInterrupt:
    pass

GPIO.cleanup()