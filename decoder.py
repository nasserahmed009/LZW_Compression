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
dictionary = []
for char in range(0,256):
    dictionary.append(chr(char))

print("⌛️ Decoding the file, please wait ..")        
output = ""
idx = 0

minValueWithLength = 128
variableLengthSize = 8

while(idx <len(binaryString)):

    if(len(dictionary) > minValueWithLength*2):
        minValueWithLength = minValueWithLength*2
        variableLengthSize = math.ceil( math.log(len(dictionary),2) )

    currentChar = int( binaryString[idx : idx+variableLengthSize], 2)
    dictionary[-1] = dictionary[-1].replace("undefined", dictionary[currentChar][0])
    
    output += dictionary[currentChar] 
    idx += variableLengthSize

    if(idx < len(binaryString)):
        dictionary.append(dictionary[currentChar] + 'undefined')


encodedTextFile = open("decoded.txt", "w")
encodedTextFile.write(output)
encodedTextFile.close()

endTime = timeit.default_timer()
print('⏱ Time taken: ', endTime - startTime)  