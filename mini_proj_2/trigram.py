<<<<<<< HEAD
from nltk.util import ngrams
import string
fp = open("corpus.txt")
n = 3
lines = map(str.strip , fp.readlines())
for line in lines :
	for c in string.punctuation:
		line = line.replace(c," ")
		print line
		trigrams = ngrams(line.split(), 3)
		for grams in trigrams:
			print grams
=======
import nltk
from math import log
import re
from collections import defaultdict

words = nltk.word_tokenize("~ ~ "+open("corpus2.txt").read().lower()+" ~ ~")
cleaned_words = []
punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')' ]
two_words = defaultdict(int)
three_words = defaultdict(int)

for word in words:
	if(not (word in punctuation)):
		word = re.sub(r'[,.\'`]','',word)
		if(len(word) > 0):
			cleaned_words.append(word)

for i in range(len(cleaned_words)-2):
	two_words[(cleaned_words[i], cleaned_words[i+1])] += 1
	three_words[(cleaned_words[i], cleaned_words[i+1], cleaned_words[i+2])] += 1

for key,value in three_words.iteritems():
	q_ML = float(value)/two_words[(key[0],key[1])]
	print key[0]+","+key[1]+","+key[2]+","+str(q_ML)+","+str(log(q_ML))
>>>>>>> d4de9b21ef3077a92fb0fab67dcadaeeb2bf0292
