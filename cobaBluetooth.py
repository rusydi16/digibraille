import bluetooth

def konversi(huruf):
	if huruf == b'a' or huruf == b'1':
		return '100000'
	elif huruf == b'b' or huruf == b'2':
		return '110000'
	elif huruf == b'c' or huruf == b'3':
		return '100100'
	elif huruf == b'd' or huruf == b'4':
		return '100110'
	elif huruf == b'e' or huruf == b'5':
		return '100010'
	elif huruf == b'f' or huruf == b'6':
		return '110100'
	elif huruf == b'g' or huruf == b'7':
		return '110110'
	elif huruf == b'h' or huruf == b'8':
		return '110010'
	elif huruf == b'i' or huruf == b'9':
		return '010100'
	elif huruf == b'j' or huruf == b'0':
		return '010110'
	elif huruf == b'k':
		return '101000'
	elif huruf == b'l':
		return '100100'
	elif huruf == b'm':
		return '101100'
	elif huruf == b'n':
		return '101110'
	elif huruf == b'o':
		return '101010'
	elif huruf == b'p':
		return '111100'
	elif huruf == b'q':
		return '111110'
	elif huruf == b'r':
		return '111010'
	elif huruf == b's':
		return '011010'
	elif huruf == b't':
		return '011110'
	elif huruf == b'u':
		return '101001'
	elif huruf == b'v':
		return '111001'
	elif huruf == b'w':
		return '010111'
	elif huruf == b'x':
		return '101101'
	elif huruf == b'y':
		return '101111'
	elif huruf == b'z':
		return '101011'

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)
while 1:
    input_now = client_socket.recv(1024)
    print ("Received: %s" % input_now)
#for h in range(len(input_now)):
    braille = konversi(input_now)
    b1 = int(braille[0])
    b2 = int(braille[1])
    b3 = int(braille[2])
    b4 = int(braille[3])
    b5 = int(braille[4])
    b6 = int(braille[5])
    print (b1, b2, b3, b4, b5, b6)
    
client_socket.close()
server_socket.close()
