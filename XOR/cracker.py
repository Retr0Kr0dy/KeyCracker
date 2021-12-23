from hashlib import sha256
import hashlib
import random
import string
import os

file_to_crypt = input ("\nEnter the name of the file to crack :")
output = input ("\nEnter the name of output file :")
number = int(input("\nEnter key lenght : "))
letter = input("\nEnter possible alphabet (leave empty fot only alphabetic) :")
if len(letter) == 0:
    letter = 'abcdefghijklmnopqrstuvwxyz' 
cwd = os.getcwd()
output_path = cwd + "\\" + output

z = 0

for z in range(1, 100000000) :
    i = 0
    def randStr(chars = string.ascii_uppercase + string.digits, N=number):
        return ''.join(random.choice(chars) for _ in range(N))

    word_key = randStr(chars=letter)

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
        chad = text_block_2.decode('utf-8')
        print (chad) 
        if word_key == "test":
            print(f"\n\n\nfor key {word_key} LIGMA {z}")
            input ("Key Cracked!!!(press enter to exit)")
            os.system(command)
        if "this" in chad:
            os.system(command)
            print ("DONE")
            exit(-1)
        else:
            print("you madafaka")
    except:
        print(f"for key {word_key} LIGMA {z}")
    z = z + 1 
