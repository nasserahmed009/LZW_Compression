import numpy as np
import math
import timeit

startTime = timeit.default_timer()

encodedBinaryFile = open("encoded.bin", "rb")
encodedArray = encodedBinaryFile.read()
numOfZerosAtEnd = encodedArray[0]

print("⌛️ Constructing the binary string, please wait ..")     
binaryString = ""
for val in encodedArray:
    binaryString += format(val, '08b')

binaryString = binaryString[8:len(binaryString)-numOfZerosAtEnd]

# forming the initial dictionary
dictionary = np.load('dictionary.npy')
dictionary = dictionary.tolist()
# for char in range(0,256):
#     dictionary.append(chr(char))



print("⌛️ Decoding the file, please wait ..")        
output = ""
idx = 0



while(idx <len(binaryString)):

    variableLengthSize = math.ceil( math.log(len(dictionary),2) )
    
    currentChar = int( binaryString[idx : idx+variableLengthSize], 2)
    if(idx != 0):
        dictionary[-1] += dictionary[currentChar][0]
    
    output += dictionary[currentChar] 
    idx += variableLengthSize
    if(idx < len(binaryString)):
        dictionary.append(dictionary[currentChar])

    

encodedTextFile = open("decoded.txt", "w")
encodedTextFile.write(output)
encodedTextFile.close()

endTime = timeit.default_timer()
print('⏱ Time taken: ', endTime - startTime)  