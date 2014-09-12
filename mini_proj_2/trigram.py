import nltk
from math import log
import re

words = nltk.word_tokenize(open("corpus2.txt").read().lower())
cleaned_words = []
punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')' ]
for word in words:
	if(not (word in punctuation)):
		cleaned_words.append(re.sub(r'[,.\']','',word))

bigrams = [(cleaned_words[x], cleaned_words[x+1]) for x in range(len(cleaned_words) -1)]

trigrams = [(cleaned_words[x], cleaned_words[x+1], cleaned_words[x+2]) for x in range(len(cleaned_words) - 2)]

for trigram in trigrams:
    q_ML = float(trigrams.count(trigram))/bigrams.count((trigram[0], trigram[1]))
    print trigram[0]+","+trigram[1]+","+trigram[2]+","+str(q_ML)+","+str(log(q_ML))+"\n"