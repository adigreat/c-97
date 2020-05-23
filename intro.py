introString=input("enter your intoduction")
print(introString)
charcount=0
wordcount=1
for i in introString:
    charcount=charcount+1
    if(i==' '):
        wordcount=wordcount+1
   
print("no of words in the string: ")
print(wordcount)
print("no of charachters in the string")
print(charcount)