
import _io
import re

outputStream = open("preprocessed_tweets.txt",'w',encoding='UTF-8')
with open("tweets.txt", 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
            temp = ""
            for val in line.split(" "):
                  if (re.fullmatch('[a-zA-Z|i|ş|ö|ğ|ç|ü|â|ı|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+', val)):
                        #The output should be consisting of only letters.
                        temp = temp + " " + val
                  elif (re.fullmatch('[@][a-zA-Z|i|ş|ö|ğ|ç|ü|ı|x|â|İ|Ü|Ğ|Ç|Ö|X|Ş]+', val)):
                        #The words starting with “@” should be also ignored.
                        continue
                  elif (re.fullmatch('[1-9|“|:|"|…|;|?|!|{|\'|}|(|)|,|.|-|_]*[a-zA-Z|i|â|ş|ö|ğ|ç|ü|ı|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+[1-9|”|:|"|;|…|\'|?|!|{|}|(|)|@|,|.|-|_]*', val)):
                        #Punctuation marks and numbers before and at the end of the word should be deleted.
                        temp = temp + " " + re.sub('[1-9|”|“|:|"|…|;|\'|?|!|{|}|(|)|@|,|.|-|_]', '', val)
                        continue
                  elif (re.fullmatch('[a-zA-Z|i|ş|ö|ğ|ç|â|ü|ı|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+[1-9|”|:|"|…|;|?|!|\'|{|}|(|)|@|,|.|-|_]+[a-zA-Z|i|ş|ö|â|ğ|ç|ü|ı|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+', val)):
                        #If there is a punctuation mark or/and number in the middle of the word, that word should be ignored.
                        temp = temp + " " + val
            if(not temp.__eq__("")):
                  outputStream.write(temp[1:temp.__len__()] + "\n")    
            
outputStream.close()
file.close()
            