'''#Longest word in a file

#inf=False
try:
    inf=open("hai.txt",'w+')
    lines=inf.read().split()
    lines.sort(key=len,reverse=True)
    
    l=len(lines[0])
    print([x for x in lines if len(x)==l])
except IOError as e :
    print(e)
finally:
    if inf:inf.close() '''

# input text file
inputFile = "hai.txt"

# Opening the given file in read-only mode.
with open(inputFile, 'r') as filedata:

# Getting the list of words of a file
                       wordsList = filedata.read().split()

# finding the length of the longest word in the above words list
longestWordLength = len(max(wordsList, key=len))

# Storing all the words having the maximum length(longest word length)

# Here, we are checking all the words whose length is equal to that of the longest word
result = [textword for textword in wordsList if len(textword) == longestWordLength]

# Print the longest words from a text file
print("The following are the longest words from a text file:")
print(result)

# Closing the input file
filedata.close()
