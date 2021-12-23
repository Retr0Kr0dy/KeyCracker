import os
import blowfish
import time

file_to_crypt = input ("\n\nEnter the name of the file to crack :")
output = input ("\n\nEnter the name of output file :")
cwd = os.getcwd()
output_path = cwd + "\\" + output

with open (file_to_crypt, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()

z = 1

for z in range(1, 10000000):
    iv = os.urandom(8)                
    key = os.urandom(56)
    hashnsalt = blowfish.Cipher(key)
    try:
        data_result = b"".join(hashnsalt.decrypt_cfb(text_block, iv))
    except:
        print(f'FUCKKK {z}')    
    print(f'For key: {key} iv: {iv}; done : {data_result}')
    la_phrase = f'For key: {key} iv: {iv}; done : {data_result}'
    command = f'cmd /c "echo {la_phrase} >> {output_path} "'
    try:
        chad = data_result.decode('utf-8')
        print (chad) 
        if "this" in chad:
            os.system(command)
            print ("DONE")
            exit(-1)
        else:
            print("you madafaka")
    except:
        print(f"LIGMA {z}")
    z = z + 1 
