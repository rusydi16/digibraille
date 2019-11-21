# mengimport library yang diperlukan
import RPi.GPIO as GPIO #library GPIO
import time #library waktu
import string

B1 = 4 #GPIO3 yang akan disambungkan ke LED
B2 = 5
B3 = 6
B4 = 7
B5 = 8
B6 = 9

def insert_angka(h, word):
	if h != 0:
		kata = word[:h]+'#'+word[h:]
		return kata
	else:
		kata = '#' + word[h:]
		return kata

def insert_hurufBesar(h, word):
	if h != 0:
		kata = word[:h]+'~'+word[h:]
		return kata
	else:
		kata = '~' + word[h:]
		return kata

def kembali_huruf(h, word):
	kata = word[:h]+';'+word[h:]
	return kata

def huruf_besar_semua(word):
	kata = '~~' + word
	return kata

def konversi(huruf):
	if huruf == 'a' or huruf == '1':
		return '100000'
	elif huruf == 'b' or huruf == '2':
		return '110000'
	elif huruf == 'c' or huruf == '3':
		return '100100'
	elif huruf == 'd' or huruf == '4':
		return '100110'
	elif huruf == 'e' or huruf == '5':
		return '100010'
	elif huruf == 'f' or huruf == '6':
		return '110100'
	elif huruf == 'g' or huruf == '7':
		return '110110'
	elif huruf == 'h' or huruf == '8':
		return '110010'
	elif huruf == 'i' or huruf == '9':
		return '010100'
	elif huruf == 'j' or huruf == '0':
		return '010110'
	elif huruf == 'k':
		return '101000'
	elif huruf == 'l':
		return '100100'
	elif huruf == 'm':
		return '101100'
	elif huruf == 'n':
		return '101110'
	elif huruf == 'o':
		return '101010'
	elif huruf == 'p':
		return '111100'
	elif huruf == 'q':
		return '111110'
	elif huruf == 'r':
		return '111010'
	elif huruf == 's':
		return '011010'
	elif huruf == 't':
		return '011110'
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
		return '011000'
	elif huruf == ',':
		return '010000'

def output(pin,con):
    if con == 1:
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)
    return


# mengatur mode GPIO apakah model BOARD atau BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(B1,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)
GPIO.setup(B3,GPIO.OUT)
GPIO.setup(B4,GPIO.OUT)
GPIO.setup(B5,GPIO.OUT)
GPIO.setup(B6,GPIO.OUT)

try:
    while(1):
        input_now = input("Masukkan kata: ")
        print(input_now)
        if input_now.isupper():
            input_now = huruf_besar_semua(input_now)
            
        h = 0
        status = 0

        while(h<len(input_now)):
            if input_now[h].isdigit():
                    if status == 1 :
                            h=h+1
                    else:
                            input_now = insert_angka(h,input_now)
                            h=h+2
                            status = 1
            elif input_now[h] in string.punctuation:
                    h=h+1
            else:
                    if status == 1 :
                            if input_now[h].isupper():
                                    input_now = kembali_huruf(h,input_now)
                                    input_now = insert_hurufBesar(h+1, input_now)
                                    h=h+3
                                    status = 0
                            else:
                                    input_now = kembali_huruf(h,input_now)
                                    h=h+2
                                    status = 0
                    else:
                            if input_now[h].isupper():
                                    input_now = insert_hurufBesar(h, input_now)
                                    h=h+2
                            else:
                                    h=h+1

        input_now = input_now.lower()
        print("Hasil Modifikasi Kata =", input_now)
        
        for h in range (len(input_now)):
            braille = konversi(input_now[h])
            output(B1,int(braille[0]))
            output(B2,int(braille[1]))
            output(B3,int(braille[2]))
            output(B4,int(braille[3]))
            output(B5,int(braille[4]))
            output(B6,int(braille[5]))
            print(braille)
            time.sleep(5)
                        
except KeyboardInterrupt:
    GPIO.cleanup() #exit


