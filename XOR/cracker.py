from hashlib import sha256
import hashlib
import random
import string
import os

file_to_crypt = input ("\nEnter the name of the file to crack :")
output = input ("\nEnter the name of output file :")
def take_number():
    global number_input
    number_input = input("\nEnter key lenght (leave empty for random lenght): ")
    if len(number_input) == 0:
        global num_a
        global num_b
        num_a = int(input ("\nSelect start size lenght :"))
        num_b = int(input ("\nSelect final size lenght :"))
    else:
        global number
        number = int(number_input)
take_number()
def take_letter():
    global letter
    letter = input("\nEnter possible alphabet (leave empty for help) :")
    if letter == "ALPHA" or letter == "alpha":
        letter = 'abcdefghijklmnopqrstuvwxyz' 
    if letter == "ALPHANUM" or letter == "alphanum":
        letter = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if letter == "ALL" or letter == "all":
        letter = 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&''()[]}{~-|`_\\@=+-*/§.,?:;ùµ£¤^¨' 
    if len(letter) == 0:
        print("\nHELP\n\nALPHA or alpha ; alphabetic\nALPHANUM or alphanum ; alpha-numeric\nALL or all ; all ascii character")
        take_letter()
take_letter() 
cwd = os.getcwd()
output_path = cwd + "\\" + output
z = 0
list = []
for z in range(1, 100000000) :
    i = 0
    if len(number_input) == 0:
        number = random.randint(num_a, num_b)
    def randStr(chars = string.ascii_uppercase + string.digits, N=number):
        return ''.join(random.choice(chars) for _ in range(N))
    word_key = randStr(chars=letter)
    list.append(word_key)
    if word_key in list:
        pre_keys = sha256(word_key.encode('utf-8')).digest()
        hash_keys = hashlib.sha512(pre_keys)
        hash_digest = hash_keys.hexdigest()
        keys = sha256(hash_digest.encode('utf-8')).digest()
        with open (file_to_crypt, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()
            text_block_2 = bytes()
        for i in range (len(text_block)):
            c = text_block[i]
            j = i % len(keys)
            b = bytes ([c^keys[j]])
            text_block_2 = text_block_2 + b
        la_phrase = f'For key : {word_key} ; done : {text_block_2}'
        command = f'cmd /c "echo {la_phrase} >> {output_path} "'
        try:
            chad = text_block_2.decode('ascii')
            print ("\n" + chad) 
            print(f"\nfor key {word_key} LIGMA {z}")
            blablabla = input ("\nKey Cracked!!!(press enter to exit or type continue to follow cracking)")
            if blablabla == "continue":
                print("CONTINUING!!!")
            else:
                os.system(command)
                print (list)
                break
        except:
            print(f"for key {word_key} LIGMA {z}")
    z = z + 1 
