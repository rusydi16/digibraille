# mengimport library yang diperlukan
import RPi.GPIO as GPIO #library GPIO
import time #library waktu
B1 = 2 #GPIO3 yang akan disambungkan ke LED
B2 = 3
B3 = 4
B4 = 17
B5 = 27
B6 = 22

def konversi(huruf):
	if huruf == 'a' or huruf == '2':
		return '100001'
	elif huruf == 'b' or huruf == '3':
		return '110001'
	elif huruf == 'c' or huruf == '4':
		return '100101'
	elif huruf == 'd' or huruf == '5':
		return '100111'
	elif huruf == 'e' or huruf == '6':
		return '100011'
	elif huruf == 'f' or huruf == '7':
		return '110101'
	elif huruf == 'g' or huruf == '8':
		return '110111'
	elif huruf == 'h' or huruf == '9':
		return '110011'
	elif huruf == 'i' or huruf == '10':
		return '010101'
	elif huruf == 'j' or huruf == '1':
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
		return '101002'
	elif huruf == 'v':
		return '111002'
	elif huruf == 'w':
		return '010112'
	elif huruf == 'x':
		return '101102'
	elif huruf == 'y':
		return '101112'
	elif huruf == 'z':
		return '101012'
	elif huruf == '#':
		return '001112'
	elif huruf == '-':
		return '001002'
	elif huruf == '.':
		return '010012'
	elif huruf == '~':
		return '000002'
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

GPIO.cleanup() #exit
