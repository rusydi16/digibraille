# mengimport library yang diperlukan
import RPi.GPIO as GPIO
import time

# mengatur mode GPIO apakah model BOARD atau BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT) # GPIO3 sebagai output LED
GPIO.setup(2,GPIO.IN) # GPIO2 sebagai input dari tombol/push button

# lampu menyala saat pushbutton ditekan
# (lampu menyala bila GPIO2 diberi ground)
while True:
    if (GPIO.input(2)==False): # maksud False adalah jika diberi 0v (ground)
        GPIO.output(3,GPIO.HIGH)
        print('nyala')
    else :
        GPIO.output(3,GPIO.LOW) #mematikan LED
        #print('mati')
