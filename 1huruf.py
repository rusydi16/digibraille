# mengimport library yang diperlukan
import RPi.GPIO as GPIO #library GPIO
import time #library waktu
import string
from bluetooth import *

B1 = 5 #GPIO4 Data 1
B2 = 4 #GPIO5 Data 2
B3 = 8 #GPIO6 CLOCK 1
B4 = 9 #GPIO7 Latch 1
B5 = 6 #GPIO8 Clock 2
B6 = 7 #GPIO9 Latch 2

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

def clock(pin_clock):
    GPIO.output(pin_clock,GPIO.HIGH)
    time.sleep(.01)
    GPIO.output(pin_clock,GPIO.LOW)
    return
    
def latch(pin_latch):
    GPIO.output(pin_latch,GPIO.HIGH)
    time.sleep(.01)
    GPIO.output(pin_latch,GPIO.LOW)
    return
    
def reset(pin, pin_clock, pin_latch):
    for x in range(0,8):
        GPIO.output(pin,GPIO.LOW)
        clock(pin_clock)
    latch(pin_latch)
    return

# mengatur mode GPIO apakah model BOARD atau BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(B1,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)
GPIO.setup(B3,GPIO.OUT)
GPIO.setup(B4,GPIO.OUT)
GPIO.setup(B5,GPIO.OUT)
GPIO.setup(B6,GPIO.OUT)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
                   
print("Menunggu Koneksi dari RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Koneksi tersambung dari ", client_info)

try:
    while(1):
        input_now = client_sock.recv(1024)
        #if len(input_now) == 0: break
        #print("received [%s]" % data)
        
        #input_now = input("Masukkan kata: ")
        
        input_now=input_now.decode('utf-8')
        print(input_now)
        
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
        
        i=0
        while(i<len(input_now)):
            if((input_now[i]==';' or input_now[i]=='~' or input_now[i]=='#')and i<=len(input_now)-1 and input_now[i+1].isalpha()):
                braille = konversi(input_now[i])
                print(braille)
                for x in range (len(braille)):
                    output(B1,int(braille[x]))
                    clock(B3)
                
                braille = konversi(input_now[i+1])
                print(braille)
                for x in range (len(braille)):
                    output(B2,int(braille[x]))
                    clock(B5)
                latch(B4)
                latch(B6)
                i = i+2
            elif ((i <=(len(input_now)-2) and input_now[i]==';' and input_now[i+1]=='~' and input_now[i+2].isalpha())):
                braille = konversi(input_now[i])
                print(braille)
                for x in range (len(braille)):
                    output(B1,int(braille[x]))
                    clock(B3)
                
                braille = konversi(input_now[i+1])
                print(braille)
                for x in range (len(braille)):
                    output(B2,int(braille[x]))
                    clock(B5)
                latch(B4)
                latch(B6)
                i = i+2
            else:
                braille = konversi(input_now[i])
                print(braille)
                for x in range (len(braille)):
                    output(B2,int(braille[x]))
                    clock(B5)
                latch(B6)
                i=i+1
            time.sleep(1)
            reset(B1,B3,B4)
            reset(B2,B5,B6)
            
                        
except KeyboardInterrupt or IOError:
    GPIO.cleanup() #exit
    
    print("disconnected")

    client_sock.close()
    server_sock.close()
    print("all done")
    pass
    

