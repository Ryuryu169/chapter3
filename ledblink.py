import time
import RPi.GPIO as GPIO

# GPIO.BCMを指定するとGPIO番号モードで指定
# GPIO.BOARDを指定するとpin番号モードで指定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO14を出力に設定
GPIO.setup(14, GPIO.OUT)

while(1):
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(14, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
