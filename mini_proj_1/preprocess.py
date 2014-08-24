import re
from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import defaultdict
from math import log

fp = open("cri.txt")
content = eval(fp.read())
docs = []
processed_docs = []
stemmer = PorterStemmer()
idfs = defaultdict(int)
tfs = []

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def idf_calc():
	for doc in processed_docs:
		doc = remove_duplicates(doc)
		for word in doc:
			idfs[word] += 1
	for key,value in idfs.iteritems():
		idfs[key] = log((1.0*len(content))/value)

def tf_calc():
	for doc in processed_docs:
		tf = defaultdict(int)
		for word in doc:
			tf[word] += 1
		for key,value in tf.iteritems():
			tf[key] = (1.0*value)/len(doc)
		tfs.append(tf)

def normalize():
	stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'between', 'into','to', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'in', 'on', 'under', 'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor',  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
	punctuation = [',', '.', '?', '!']
	for doc in content:
		doc = re.sub(r'(,)([0-9]+)', r"\1 \2", doc.lower())
		doc = wt(doc)
		sentence = []
		for word in doc:
			if word not in stop and word not in punctuation:
				sentence.append(stemmer.stem(word))
		processed_docs.append(sentence)

def main():
	normalize()
	tf_calc()
	idf_calc()
	print idfs

if __name__ == '__main__':
	main()
