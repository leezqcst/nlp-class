import nltk
from collections import defaultdict
import re
import random
from math import log

words = nltk.word_tokenize(open("corpus1n.txt").read().decode('utf-8').lower())
uni = defaultdict(int)

stop = set()
start = set()
for sentence in open("corpus1n.txt").read().decode('utf-8').encode('ascii', 'ignore').lower().split("."):
	sentence = re.sub(r'[\n\r]', '', sentence)
	if(len(sentence) > 0):
		stop.add(sentence.split(" ")[-1])
		start.add(sentence.split(" ")[0])

cleaned_words = []
punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')' ,'[', ']']
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

i = 0
output = []
output.append(random.choice(list(start)))

# print [word for word in three_words if word[0] == output[-1]]

while True:
	if (i > 15 and word[2] in stop):
		break
	else:
		wordlist = [word for word in three_words if word[0] == output[-1]]
		if (len(wordlist) > 0):
			word = random.choice(wordlist)
			output.append(word[1])
			output.append(word[2])
		else:
			break
	i = i + 1
print ' '.join(output)