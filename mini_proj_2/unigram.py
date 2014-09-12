import nltk
from collections import defaultdict
import re
from math import log

words = nltk.word_tokenize(open("corpus1.txt").read().lower())
uni = defaultdict(int)

punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&' ]
count = 0
for word in words:
	if(not word in punctuation):
		word = re.sub(r'[,.\']','',word)
		uni[word] += 1
		count += 1

for key,value in uni.iteritems():
	probab = (1.0*value)/count
	print key+","+str(probab)+","+str(log(probab))+"\n"