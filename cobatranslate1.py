# mengimport library yang diperlukan
# import RPi.GPIO as GPIO  # library GPIO
import time  # library waktu
import string


def insert_angka(h, word):
    if h != 0:
        kata = word[:h] + '#' + word[h:]
        return kata
    else:
        kata = '#' + word[h:]
        return kata


def insert_hurufBesar(h, word):
    if h != 0:
        kata = word[:h] + '~' + word[h:]
        return kata
    else:
        kata = '~' + word[h:]
        return kata


def kembali_huruf(h, word):
    kata = word[:h] + ';' + word[h:]
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
    elif huruf == ':':
        return '010010'
    elif huruf == '?':
        return '011001'
    elif huruf == '!':
        return '011010'
    elif huruf == ',':
        return '010000'
    elif huruf == ' ':
        return '000000'
    elif huruf == '\'':
        return '001101'
    elif huruf == '(' or huruf == ')':
        return '011011'
    elif huruf == '-':
        return '001001'
    elif huruf == '/':
        return '001100'
    elif huruf == '*':
        return '001010'
    elif huruf == '=':
        return '010010'
    elif huruf == '\n' or huruf == '\r\n':
        return '000000'


try:
    while 1:
        input_now = input("Masukkan:")
        print(input_now)

        h = 0
        status = 0

        while h < len(input_now):
            if input_now[h].isdigit():
                if status == 1:
                    h = h + 1
                else:
                    input_now = insert_angka(h, input_now)
                    h = h + 2
                    status = 1
            elif input_now[h] in string.punctuation:
                if input_now[h] == '.' and input_now[h - 1].isdigit() and input_now[h + 1].isdigit():
                    input_now[h] = ','
                h = h + 1
            else:
                if status == 1:
                    if input_now[h].isupper():
                        input_now = kembali_huruf(h, input_now)
                        input_now = insert_hurufBesar(h + 1, input_now)
                        h = h + 3
                        status = 0
                    else:
                        input_now = kembali_huruf(h, input_now)
                        h = h + 2
                        status = 0
                else:
                    if input_now[h].isupper():
                        input_now = insert_hurufBesar(h, input_now)
                        h = h + 2
                    else:
                        h = h + 1

        input_now = input_now.lower()
        print("Hasil Modifikasi Kata =", input_now)

        i = 0
        while i < len(input_now):
            if ((input_now[i] == ';' or input_now[i] == '~' or input_now[i] == '#') and i <= len(input_now) - 1 and
                    input_now[i + 1].isprintable()):
                braille = konversi(input_now[i])
                print("bit1=", braille)

                braille = konversi(input_now[i + 1])
                print("bit2=", braille)
                i = i + 2
                print('hoho')
            elif i <= (len(input_now) - 2) and input_now[i] == '"' and (
                    input_now[i - 1] == ' ' or i == 0 or input_now[i + 1] in string.printable):
                braille = '011001'
                print("bit2=", braille)
                i = i + 1
            elif input_now[i] == '"' and input_now[i - 1] in string.printable and input_now[i - 1] != ' ':
                braille = '001011'
                print("bit2=", braille)
                i = i + 1
            elif i <= (len(input_now) - 2) and input_now[i] == '\'' and (
                    input_now[i - 1] == ' ' or i == 0 or input_now[i + 1] in string.printable):
                braille = konversi('~')
                print("bit1=", braille)

                braille = '011001'
                print("bit2=", braille)
                i = i + 1
            elif input_now[i] == '\'' and input_now[i - 1] in string.printable and input_now[i - 1] != ' ':
                braille = '001011'
                print("bit1=", braille)

                braille = konversi('~')
                print("bit2=", braille)
                i = i + 1
            elif (input_now[i] == '-' and input_now[i + 1] == '-') or input_now[i] == '*' or input_now[i] == '=':
                braille = konversi(input_now[i])
                print("bit1=", braille)

                braille = konversi(input_now[i])
                print("bit2=", braille)

                i = i + 1
            elif input_now[i] == '<':
                braille = konversi(':')
                print("bit1=", braille)
                if input_now[i + 1] == '=':
                    braille = '011011'
                    print("bit1=", braille)
                    i = i + 2
                else:
                    braille = '100100'
                    print("bit2=", braille)
                    i = i + 1
            elif input_now[i] == '<':
                braille = konversi(':')
                print("bit1=", braille)
                if input_now[i + 1] == '=':
                    braille = konversi('(')
                    print("bit1=", braille)
                    i = i + 2
                else:
                    braille = '100100'
                    print("bit2=", braille)
                    i = i + 1
            else:
                braille = konversi(input_now[i])
                print("bit2=", braille)

                i = i + 1
            time.sleep(1)

except KeyboardInterrupt or IOError:
    print("all done")
    pass
