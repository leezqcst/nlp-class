import re
from nltk.tokenize import word_tokenize as wt
fp = open("cri.txt")
content = eval(fp.read())
docs = []
processed_docs = []
for doc in content:
	docs.append(doc.lower())

for doc in docs:
	processed_docs.append(wt(doc))

print processed_docs


