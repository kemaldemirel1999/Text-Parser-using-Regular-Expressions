# Tweet-Parser-using-Regular-Expressions
Python script named preprocess_text.py that will clean (remove non-letter characters) text file in the given input text file. This program should read tweets.txt to preprocess text

This program should read tweets.txt to preprocess text, the program should be run as:
$ python preprocess_text.py

The program must produce the output file preprocessed_tweets.txt. The program should read the input file line by line. The output should be consisting of only letters. Punctuation marks and numbers before and at the end of the word should be deleted.
If there is a punctuation mark or/and number in the middle of the word, that word should be ignored. The words starting with “@” should be also ignored. (Example: https://t.co/7eCzBgVOhs and @bil334 should be ignored)

Example Input File

@asirihaklii: Psikoloji der ki: “Bulunduğun anı tekrar yaşayamacağının bilincinde olursan hayat sana daha anlamlı gelir”

@madrigalofc: gece sabaha kadar burda oturup hayatı sorgulamak istiyorum https://t.co/b5n1dHungE

@spotifysozleri: ''Bu yol nereye gider bilmem ama yürüyorum işte.''

@picvsco: Şunlara bayıldım https://t.co/7eCzBgVOhs

Example Output File

Psikoloji der ki Bulunduğun anı tekrar yaşayamacağının bilincinde olursan hayat sana daha anlamlı gelir

gece sabaha kadar burda oturup hayatı sorgulamak istiyorum

Bu yol nereye gider bilmem ama yürüyorum işte

Şunlara bayıldım
