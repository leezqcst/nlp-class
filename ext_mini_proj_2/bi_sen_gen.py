import nltk
from collections import defaultdict
import re
import random
from math import log

words = nltk.word_tokenize(open("Corpus 1.txt").read().lower())
uni = defaultdict(int)

start_words = set()
end_words = set()
cleaned_words = []

fp = open("Corpus 1.txt","r")
lines = fp.read() 
for line in lines.lower().split("."):
	line = re.sub(r'[\n\r]', '', line)
	if(len(line) > 0):
		start_words.add(line.split(" ")[0])
		end_words.add(line.split(" ")[-1])


punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')','vs.','[',']','-' ]
bigrams = defaultdict(int)

for word in words:
	if(not (word in punctuation)):
		word = re.sub(r'[,.\'`]','',word)
		if(len(word) > 0):
			cleaned_words.append(word)

for i in range(len(cleaned_words)-1):
	bigrams[(cleaned_words[i], cleaned_words[i+1])] += 1

i = 0
sentence = []
sentence.append(random.choice(list(start_words)))

while True:
	if (i > 15 and word[1] in end_words):
		break
	else:
		wordlist = [word for word in bigrams if word[0] == sentence[-1]]
		if (len(wordlist) > 0):
			word = random.choice(wordlist)
			sentence.append(word[1])
		else:
			break
	i = i + 1
print ' '.join(sentence)
