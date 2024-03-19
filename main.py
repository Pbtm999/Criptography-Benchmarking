from randomFiles import createFile
from AES import AESEncrypt
from SHA import SHAGen256
from RSA import RSAAlg
import matplotlib.pyplot as plt

createFile('AES', 8)
createFile('SHA', 8)
createFile('RSA', 2)

AESlistE = [0]*7
AESlistD = [0]*7
SHAlist = [0]*7
RSAlistE = [0]*7
RSAlistD = [0]*7

for i in range(0,3):
    AESlistE, AESlistD = AESEncrypt(AESlistE, AESlistD)
    SHAlist = SHAGen256(SHAlist)
    RSAlistE, RSAlistD = RSAAlg(RSAlistE, RSAlistD)

AESlistE[:] = [x / 3 for x in AESlistE]
AESlistD[:] = [x / 3 for x in AESlistD]
RSAlistE[:] = [x / 3 for x in RSAlistE]
RSAlistD[:] = [x / 3 for x in RSAlistD]
SHAlist[:] = [x / 3 for x in SHAlist]

plt.plot([8,64,512,4096,32768,262144,2097152], AESlistE)
plt.axis([8,4096, 0, 0.005])
plt.show()
plt.plot([8,64,512,4096,32768,262144,2097152], AESlistD)
plt.axis([8,2097152, 0, 0.005])
plt.show()
plt.plot([8,64,512,4096,32768,262144,2097152], SHAlist)
plt.axis([8,2097152, 0, 0.005])
plt.show()
plt.plot([2,4,8,16,32,64,128], RSAlistE)
plt.axis([2,128, 0, 0.005])
plt.show()
plt.plot([2,4,8,16,32,64,128], RSAlistD)
plt.axis([2,128, 0, 0.005])
plt.show()
