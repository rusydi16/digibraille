# mengimport library yang diperlukan
import RPi.GPIO as GPIO #library GPIO
import time #library waktu
pin = 3 #GPIO3 yang akan disambungkan ke LED

# membuat fungsi blink
def blink(pin):
    GPIO.output(pin,GPIO.HIGH) # menyalakan LED
    print('nyala')
    time.sleep(3) # delay 1 detik
    GPIO.output(pin,GPIO.LOW) # mematikan LED
    print('mati')
    time.sleep(3) # delay 1 detik
    return

# mengatur mode GPIO apakah model BOARD atau BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT) # “pin” yang dimaksud adalah GPIO3
for i in range(0,9):
    blink(pin)

GPIO.cleanup() #exit
