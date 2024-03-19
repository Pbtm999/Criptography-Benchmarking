from os import urandom
from binascii import hexlify
from cryptography .hazmat. primitives . ciphers import Cipher , algorithms , modes
from cryptography.hazmat.primitives import padding
import time

def AESEncrypt(AESlistE, AESlistD):
    for i in range(1, 8):
        f = open('AES/' + str(8**i) + 'bytesRandom.txt', "r")
        fileData = bytes(f.read(), encoding= 'utf-8')
        f.close ()

        start = time.time()

        key = urandom(32)
        if (8**i%16 != 0):
            padder = padding.PKCS7(256).padder()
            fileData = padder.update(fileData)
            fileData += padder.finalize()

        cipher = Cipher( algorithms.AES(key), modes.ECB())

        encryptor = cipher.encryptor()
        ct = encryptor.update(fileData) + encryptor.finalize()

        end = time.time()
        AESlistE[i-1] += (end-start)
        print(str(8**i) + ' bytes AES encrypt takes ' + str(end-start) + ' sec')

        start = time.time()

        decryptor = cipher.decryptor()
        ct = decryptor.update(ct) + decryptor.finalize()

        if (8**i%16 != 0):
            unpadder = padding.PKCS7(256).unpadder()
            ct = unpadder.update(ct)
            ct += unpadder.finalize()

        end = time.time()
        AESlistD[i-1] += (end-start)
        print(str(8**i) + ' bytes AES decrypt takes ' + str(end-start) + ' sec')

    print('\n')
    return AESlistE, AESlistD





