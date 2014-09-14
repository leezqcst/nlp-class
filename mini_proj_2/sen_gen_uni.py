import nltk
from collections import defaultdict
import re
import random
from math import log

words = nltk.word_tokenize(open("corpus1.txt").read().lower())
uni = defaultdict(int)

stop = set()
for sentence in open("corpus1.txt").read().lower().split("."):
	if(len(sentence) > 0):
		stop.add(sentence.split(" ")[-1])

punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&' ]
count = 0
for word in words:
	if(not word in punctuation):
		word = re.sub(r'[,.\'`]','',word)
		uni[word] += 1
		count += 1

for key,value in uni.iteritems():
	uni[key] = (1.0*value)/count

i = 0
while (True):
	word = random.choice(uni.keys())
	if(i > 7 and word in stop):
		break
	print word+" ",
	i = i+1
