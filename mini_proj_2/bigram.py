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

for bigram in bigrams:
    q_ML = 1.0*bigrams.count(bigram)/cleaned_words.count(bigram[0])
    print bigram[0]+","+bigram[1]+","+str(q_ML)+","+str(log(q_ML))+"\n"