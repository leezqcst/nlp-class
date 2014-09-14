import nltk
from math import log
from collections import defaultdict
import re
words = nltk.word_tokenize("~ "+open("corpus2.txt").read().lower()+" ~")
count = defaultdict(int)
count_bigram = defaultdict(int)

cleaned_words = []
punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')' ,'[', ']']
for word in words:
	if(not (word in punctuation)):
		word = re.sub(r'[,.\'`]','',word)
		if(len(word) > 0):
			cleaned_words.append(word)
			count[word] += 1

for i in range(len(cleaned_words)-1):
	count_bigram[(cleaned_words[i],cleaned_words[i+1])] += 1

for key,value in count_bigram.iteritems():
	q_ML = float(value)/count[key[0]]
	print key[0]+","+key[1]+","+str(q_ML)+","+str(log(q_ML))

