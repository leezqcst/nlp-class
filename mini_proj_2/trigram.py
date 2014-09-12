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
