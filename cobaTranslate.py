def insert_angka(h, word):
	if h != 0:
		return word[::h]+'~'+word[h::]
	else:
		return '~' + word[h::]

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
	elif huruf == '.':
                return '010011'
        elif huruf == ',':
                return '010000'
        elif huruf == ':':
                return '010010'
        elif huruf == '?':
                return '011001'
        elif huruf == '#':
                return '001111'
        elif huruf == '!':
                return '011010'
        elif huruf == '(' or huruf == ')':
                return '011011'
        elif huruf == '-':
                return '001001'
        elif huruf == '/':
                return '001100'

#petik " awal diganti ? 
while(1):
        input_now = input("Masukkan kata: ")
        print(input_now)

        if len(input_now)<=7:
                for h in range(len(input_now)):
                        braille = konversi(input_now[h])
                        b1 = int(braille[0])
                        b2 = int(braille[1])
                        b3 = int(braille[2])
                        b4 = int(braille[3])
                        b5 = int(braille[4])
                        b6 = int(braille[5])
                        print (b1, b2, b3, b4, b5, b6)
        else:
                potong_kata = int(len(input_now)/7)+1
                if potong_kata == 2:
                        input_now_1 = input_now[0:7]
                        for h in range(len(input_now_1)):
                                braille = konversi(input_now_1[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_2 = input_now[7::]
                        for h in range(len(input_now_2)):
                                braille = konversi(input_now_2[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                elif potong_kata == 3:
                        input_now_1 = input_now[0:7]
                        for h in range(len(input_now_1)):
                                braille = konversi(input_now_1[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_2 = input_now[7:14]
                        for h in range(len(input_now_2)):
                                braille = konversi(input_now_2[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_3 = input_now[14::]
                        for h in range(len(input_now_3)):
                                braille = konversi(input_now_3[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                else:
                        input_now_1 = input_now[0:7]
                        for h in range(len(input_now_1)):
                                braille = konversi(input_now_1[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_2 = input_now[7:14]
                        for h in range(len(input_now_2)):
                                braille = konversi(input_now_2[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_3 = input_now[14:21]
                        for h in range(len(input_now_3)):
                                braille = konversi(input_now_3[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
                        input_now_4 = input_now[21::]
                        for h in range(len(input_now_4)):
                                braille = konversi(input_now_4[h])
                                b1 = int(braille[0])
                                b2 = int(braille[1])
                                b3 = int(braille[2])
                                b4 = int(braille[3])
                                b5 = int(braille[4])
                                b6 = int(braille[5])
                                print (b1, b2, b3, b4, b5, b6)
