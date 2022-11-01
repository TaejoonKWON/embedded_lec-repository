import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)

led_list = [36, 37, 38, 40] # 리스트에 핀 번호 저장

for i in range(10):
    temp_num = random.randint(0,3) # 0부터 3 중에 랜덤하게 설정
    
    # 리스트에서 랜덤하게 정해진 숫자로 LED 점등 및 소등
    GPIO.output(led_list[temp_num],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_list[temp_num],GPIO.LOW)
    time.sleep(0.5)