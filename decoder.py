import math
import timeit

startTime = timeit.default_timer()
encodedBinaryFile = open("encoded.bin", "rb")
encodedArray = encodedBinaryFile.read()
numOfZerosAtEnd = encodedArray[0]

binaryString = ""
for index, val in enumerate(encodedArray):
        binaryString += format(val, '08b')

binaryString = binaryString[8:len(binaryString)-numOfZerosAtEnd]

dictionary = []

# forming the initial dictionary
for char in range(0,256):
    if(chr(char) not in dictionary):
        dictionary.append(chr(char))
        

# print(dictionary)
# dictionaryArray = list(dictionary.keys())

output = ""
idx = 0

while(idx <len(binaryString)-1):
    variableLengthSize = math.ceil( math.log(len(dictionary),2) )
    currentChar = int( binaryString[idx : idx+variableLengthSize], 2)
    
    
    if(dictionary[-1][-9:] == 'undefined' ):
        dictionary[-1] = dictionary[-1].replace("undefined", dictionary[currentChar][0])

    dictionary.append(dictionary[currentChar] + 'undefined')

    output += dictionary[currentChar] 

    idx+=variableLengthSize


encodedTextFile = open("decoded.txt", "w")
# encodedTextFile.write( decode(encodedText, treeHeadNode) ) 
encodedTextFile.write(output)
encodedTextFile.close()


endTime = timeit.default_timer()
print('Time: ', endTime - startTime)  