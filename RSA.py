from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes

import time

def RSAAlg(RSAlistE, RSAlistD):
    for i in range(1,8):
        
        f = open('RSA/' + str(2**i) + 'bytesRandom.txt', "r")
        filedata = bytes(f.read(), encoding='utf-8')
        f.close()
        

        private_key = rsa.generate_private_key(

            public_exponent=65537,

            key_size=2048,
        )

        public_key = private_key.public_key()
        
        start = time.time()

        ciphertext = public_key.encrypt(filedata, OAEP(
            mgf= MGF1(algorithm = hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        ))

        end = time.time()
        RSAlistE[i-1] += end-start
        print(str(2**i) + ' bytes RSA takes ' + str(end-start) + ' sec')

        start = time.time()

        plaintext = private_key.decrypt(ciphertext, OAEP(
            mgf= MGF1(algorithm = hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None

        ))

        end = time.time()
        RSAlistD[i-1] += end-start
        print(str(2**i) + ' bytes RSA decrypt takes ' + str(end-start) + ' sec')

        print('\n')
    return RSAlistE, RSAlistD
