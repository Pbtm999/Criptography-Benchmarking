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

fig, ax = plt.subplots()
x = [8,349532,699056,1048580,1398104,1747628,2097152]
plt.plot([8,64,512,4096,32768,262144,2097152], AESlistE)
plt.xticks([8,64,512,4096,32768,262144,2097152], [8,64,512,4096,32768,262144,2097152])
ax.set_xticks(x)
ax.set_xticklabels(['8','64','512','4096','32768','262144','2097152'])
plt.show()

fig, ax = plt.subplots()
x = [8,349532,699056,1048580,1398104,1747628,2097152]
plt.plot([8,64,512,4096,32768,262144,2097152], AESlistD)
plt.xticks([8,64,512,4096,32768,262144,2097152], [8,64,512,4096,32768,262144,2097152])
ax.set_xticks(x)
ax.set_xticklabels(['8','64','512','4096','32768','262144','2097152'])
plt.show()

fig, ax = plt.subplots()
x = [8,349532,699056,1048580,1398104,1747628,2097152]
plt.plot([8,64,512,4096,32768,262144,2097152], SHAlist)
plt.xticks([8,64,512,4096,32768,262144,2097152], [8,64,512,4096,32768,262144,2097152])
ax.set_xticks(x)
ax.set_xticklabels(['8','64','512','4096','32768','262144','2097152'])
plt.show()

fig, ax = plt.subplots()
x = [2,23,44,65,86,107,128]
plt.plot([2,4,8,16,32,64,128], RSAlistE)
plt.xticks([2,4,8,16,32,64,128], [2,4,8,16,32,64,128])
ax.set_xticks(x)
ax.set_xticklabels(['2','4','8','16','32','64','128'])
plt.show()

fig, ax = plt.subplots()
x = [2,23,44,65,86,107,128]
plt.plot([2,4,8,16,32,64,128], RSAlistD)
plt.xticks([2,4,8,16,32,64,128], [2,4,8,16,32,64,128])
ax.set_xticks(x)
ax.set_xticklabels(['2','4','8','16','32','64','128'])
plt.show()
