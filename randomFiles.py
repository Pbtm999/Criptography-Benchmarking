import random
import os

#for AES and SHA
def createFile(dirT, base):

    if not os.path.isdir(dirT+"/"):
        os.makedirs(dirT+"/")

    for i in range(1, 8):
        string_size = base**i
        randomText = ""

        for _ in range(string_size):
            randomText += chr(random.randint(65,90))
        
        f = open(dirT + '/' + str(string_size) +'bytesRandom.txt', "w")
        f.write(randomText)
        f.close()