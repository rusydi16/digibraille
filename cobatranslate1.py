# mengimport library yang diperlukan
import RPi.GPIO as GPIO #library GPIO
import time #library waktu

B1 = 4 #GPIO3 yang akan disambungkan ke LED
B2 = 5
B3 = 6
B4 = 7
B5 = 8
B6 = 9

def konversi(huruf):
	if huruf == 'a' or huruf == '1':
		return '100001'
	elif huruf == 'b' or huruf == '2':
		return '110001'
	elif huruf == 'c' or huruf == '3':
		return '100101'
	elif huruf == 'd' or huruf == '4':
		return '100111'
	elif huruf == 'e' or huruf == '5':
		return '100011'
	elif huruf == 'f' or huruf == '6':
		return '110101'
	elif huruf == 'g' or huruf == '7':
		return '110111'
	elif huruf == 'h' or huruf == '8':
		return '110011'
	elif huruf == 'i' or huruf == '9':
		return '010101'
	elif huruf == 'j' or huruf == '10':
		return '010111'
	elif huruf == 'k':
		return '101001'
	elif huruf == 'l':
		return '100101'
	elif huruf == 'm':
		return '101101'
	elif huruf == 'n':
		return '101111'
	elif huruf == 'o':
		return '101011'
	elif huruf == 'p':
		return '111101'
	elif huruf == 'q':
		return '111111'
	elif huruf == 'r':
		return '111011'
	elif huruf == 's':
		return '011011'
	elif huruf == 't':
		return '011111'
	elif huruf == 'u':
		return '101001'
	elif huruf == 'v':
		return '111001'
	elif huruf == 'w':
		return '010111'
	elif huruf == 'x':
		return '101101'
	elif huruf == 'y':
		return '101111'
	elif huruf == 'z':
		return '101011'
	elif huruf == '#':
		return '001111'
	elif huruf == '-':
		return '001001'
	elif huruf == '.':
		return '010011'
	elif huruf == '~':
		return '000001'
	elif huruf == ';':
		return '011001'
	elif huruf == ',':
		return '010001'

def output(pin,con):
    if con == 1:
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)
    return


# mengatur mode GPIO apakah model BOARD atau BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(B1,GPIO.OUT) # “pin” yang dimaksud adalah GPIO3
GPIO.setup(B2,GPIO.OUT)
GPIO.setup(B3,GPIO.OUT)
GPIO.setup(B4,GPIO.OUT)
GPIO.setup(B5,GPIO.OUT)
GPIO.setup(B6,GPIO.OUT)

try:
    while(1):
        input_now = input("Masukkan huruf: ")
        print(input_now)
        braille = konversi(input_now)
        output(B1,int(braille[0]))
        output(B2,int(braille[1]))
        output(B3,int(braille[2]))
        output(B4,int(braille[3]))
        output(B5,int(braille[4]))
        output(B6,int(braille[5]))
        print(braille)
except KeyboardInterrupt:
    GPIO.cleanup() #exit

