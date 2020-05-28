import numpy as np
import timeit
import math



# reading the text file
validFileName = False
while not validFileName:
    try:
        fileName = input("⚙️ Enter file name to compress : ")
        origialFile = open(fileName, "rb")
        originalText = origialFile.read()
        origialFile.close()
        validFileName = True 
    except:
        print("❌ Can't find this file, Please enter a valid file name")


startTime = timeit.default_timer()

dictionary = {}
# forming the initial dictionary
for char in range(0,256):
    dictionary[chr(char)] = len(dictionary)


# constructing the binary string
print("⌛️ Constructing the binary string, please wait ..")

binaryString = ""
idx=0
while(idx < len(originalText)-1):
    currentChar = chr(originalText[idx])
    
    idx+=1
    nextChar = chr(originalText[idx])

    while(currentChar+nextChar in dictionary):
        currentChar = currentChar+nextChar
        if(idx == len(originalText)-1):
            nextChar = ''
            break
        else:
            idx+=1
            nextChar = chr(originalText[idx])


    dictionarySize = math.ceil( math.log( len(dictionary) ,2) )
    binaryChar = format(dictionary[currentChar], '0'+str(dictionarySize)+'b')

    binaryString += binaryChar

    if((currentChar+nextChar) not in dictionary):
        dictionary[currentChar+nextChar] = len(dictionary)
     
print("⌛️ Constructing the compressed file, please wait ..")

zerosAtEnd = 8 - ( 8 if len(binaryString) % 8 == 0 else len(binaryString)%8)
binaryString += zerosAtEnd * '0'

barray = bytearray()
barray.append( int( format(zerosAtEnd, '08b'), 2) )

for i in range(0,len(binaryString),8):
    currentByte=binaryString[i:i+8]
    barray.append(int(currentByte,2))

encodedBinaryFile = open("encoded.bin", "wb")
encodedBinaryFile.write(barray)
encodedBinaryFile.close()

endTime = timeit.default_timer()
print('⏱ Time taken: ', endTime - startTime, ' seconds')  
