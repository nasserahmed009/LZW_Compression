# reading the text file
textFile = open("enwik8", "r")
originalText1 = textFile.read()
textFile.close()

# reading the text file
textFile = open("decoded.txt", "r")
originalText2 = textFile.read()
textFile.close()

same = originalText1 == originalText2

print(same)

