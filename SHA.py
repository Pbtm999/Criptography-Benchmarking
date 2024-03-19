from cryptography.hazmat.primitives import hashes
import time

def SHAGen256(SHAlist):
    for i in range(1, 8):
        f = open('SHA/' + str(8**i) + 'bytesRandom.txt', "rb")
        content = f.read()
        f.close()
        
        start = time.time()
        digest = hashes.Hash(hashes.SHA256())
        digest.update(content)
        digest.finalize()
        end = time.time()
        
        SHAlist[i-1] += end-start
        print(str(8**i) + ' bytes file SHA256 Generation takes ' + str(end-start) + ' sec')

    return SHAlist
    print('\n')