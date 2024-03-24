from os import urandom
from binascii import hexlify
from cryptography .hazmat. primitives . ciphers import Cipher , algorithms , modes
import time

def AESEncrypt(AESlistE, AESlistD):
    for i in range(1, 8):
        f = open('AES/' + str(8**i) + 'bytesRandom.txt', "r")
        fileData = bytes(f.read(), encoding= 'utf-8')
        f.close ()

        key = urandom(32)
        iv = urandom(16)

        start = time.time()

        cipher = Cipher( algorithms.AES(key), modes.CTR(iv))

        encryptor = cipher.encryptor()
        ct = encryptor.update(fileData) + encryptor.finalize()

        end = time.time()
        AESlistE[i-1] += (end-start)
        print(str(8**i) + ' bytes AES encrypt takes ' + str(end-start) + ' sec')

        start = time.time()

        decryptor = cipher.decryptor()
        ct = decryptor.update(ct) + decryptor.finalize()

        end = time.time()
        AESlistD[i-1] += (end-start)
        print(str(8**i) + ' bytes AES decrypt takes ' + str(end-start) + ' sec')

    print('\n')
    return AESlistE, AESlistD