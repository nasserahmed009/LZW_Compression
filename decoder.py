import numpy as np
import math
import timeit

# reading the encoded file
encodedBinaryFile = open("encoded.bin", "rb")
encodedArray = encodedBinaryFile.read()

# start time for the decompression process
startTime = timeit.default_timer()

numOfZerosAtEnd = encodedArray[0]

print("⌛️ Constructing the binary string, please wait ..")     
binaryString = ""
for val in encodedArray:
    binaryString += format(val, '08b')

binaryString = binaryString[8:len(binaryString)-numOfZerosAtEnd]

# forming the initial dictionary
dictionary = np.load('dictionary.npy')
dictionary = dictionary.tolist()

print("⌛️ Decoding the file, please wait ..")        
output = ""
idx = 0

variableLength = math.ceil( math.log( len(dictionary) ,2) )

while(idx <len(binaryString)):
    currentChar = int( binaryString[idx : idx+variableLength], 2)
    
    if(idx != 0):
        dictionary[-1] += dictionary[currentChar][0]
    
    output += dictionary[currentChar] 
    idx += variableLength

    if(idx < len(binaryString)):
        dictionary.append(dictionary[currentChar])
        if((len(dictionary) & (len(dictionary)-1) == 0) and len(dictionary) != 0):
            variableLength += 1

encodedTextFile = open("decoded", "w")
encodedTextFile.write(output)
encodedTextFile.close()

endTime = timeit.default_timer()
print('⏱  Decompression time: ', endTime - startTime, 'seconds')  

print('✅ File decompressed successfuly and saved as : decoded')