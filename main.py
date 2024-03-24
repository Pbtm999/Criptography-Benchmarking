from randomFiles import createFile
from AES import AESEncrypt
from SHA import SHAGen256
from RSA import RSAAlg
import matplotlib.pyplot as plt

def ShowPlot(x, y, x_ticks, labels):
    fig, ax = plt.subplots()
    plt.plot(x, y)
    plt.xticks(x, x)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(labels)
    plt.show()

# Creates the files with random content by a multiple of some bytes | Alinea A
createFile('AES', 8)
createFile('SHA', 8)
createFile('RSA', 2)

#Alinea B
def BenchmarkAESSameFiles(times):
    AESlistE = [0]*7
    AESlistD = [0]*7

    for _ in range(times):
        AESlistE, AESlistD = AESEncrypt(AESlistE, AESlistD)
    AESlistE[:] = [(x / times) * 1000000 for x in AESlistE]
    AESlistD[:] = [(x / times) * 1000000 for x in AESlistD]

    ShowPlot([8,64,512,4096,32768,262144,2097152], AESlistE, [8,349532,699056,1048580,1398104,1747628,2097152], ['8','64','512','4096','32768','262144','2097152'])
    ShowPlot([8,64,512,4096,32768,262144,2097152], AESlistD, [8,349532,699056,1048580,1398104,1747628,2097152], ['8','64','512','4096','32768','262144','2097152'])
    
# BenchmarkAESSameFiles(5000)

def BenchmarkAESRandomFiles(times):
    AESlistE = [0]*7
    AESlistD = [0]*7

    for _ in range(times):
        AESlistE, AESlistD = AESEncrypt(AESlistE, AESlistD)
        createFile('AES', 8)
    AESlistE[:] = [(x / times) * 1000000 for x in AESlistE]
    AESlistD[:] = [(x / times) * 1000000 for x in AESlistD]

    ShowPlot([8,64,512,4096,32768,262144,2097152], AESlistE, [8,349532,699056,1048580,1398104,1747628,2097152], ['8','64','512','4096','32768','262144','2097152'])
    ShowPlot([8,64,512,4096,32768,262144,2097152], AESlistD, [8,349532,699056,1048580,1398104,1747628,2097152], ['8','64','512','4096','32768','262144','2097152'])
    

# BenchmarkAESRandomFiles(1000)

#Alinea C
def BenchmarkRSA(times):
    RSAlistE = [0]*7
    RSAlistD = [0]*7

    for _ in range(times):
        RSAlistE, RSAlistD = RSAAlg(RSAlistE, RSAlistD)
    RSAlistE[:] = [(x / times) * 1000000 for x in RSAlistE]
    RSAlistD[:] = [(x / times) * 1000000 for x in RSAlistD]

    ShowPlot([2,4,8,16,32,64,128], RSAlistE, [2,23,44,65,86,107,128], ['2','4','8','16','32','64','128'])
    ShowPlot([2,4,8,16,32,64,128], RSAlistD, [2,23,44,65,86,107,128], ['2','4','8','16','32','64','128'])
    
BenchmarkRSA(100)

#Alinea D
def BenchmarkSHA(times):
    SHAlist = [0]*7

    for _ in range(times):
        SHAlist = SHAGen256(SHAlist)
    SHAlist[:] = [(x / times) * 1000000 for x in SHAlist]

    ShowPlot([8,64,512,4096,32768,262144,2097152], SHAlist, [8,349532,699056,1048580,1398104,1747628,2097152], ['8','64','512','4096','32768','262144','2097152'])

# BenchmarkSHA(5000)