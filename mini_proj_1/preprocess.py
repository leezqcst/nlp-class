import re
from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import defaultdict
from math import log

fp = open("cri.txt")
content = eval(fp.read())
docs = []
stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'between', 'into','to', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'in', 'on', 'under', 'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor',  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
punctuation = [',', '.', '?', '!']
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
	for doc in content:
		doc = re.sub(r'(,)([0-9]+)', r"\1 \2", doc.lower())
		doc = wt(doc)
		sentence = []
		for word in doc:
			if word not in stop and word not in punctuation:
				sentence.append(stemmer.stem(word))
		processed_docs.append(sentence)

def normalize_query(q):
	q = re.sub(r'(,)([0-9]+)', r"\1 \2", q.lower())
	q = wt(q)
	normalized_q = []
	for word in q:
		if word not in stop and word not in punctuation:
			normalized_q.append(word)
	return normalized_q


def query():
	query = raw_input("Enter query : ")
	query = normalize_query(query)
	return query

def rank(q):
	ranking = []
	for i,doc in enumerate(processed_docs):
		rank = 0
		for word in q:
			if word in doc:
				rank += tfs[i][word] * idfs[word]
		ranking.append((rank,i))
	ranking.sort(key = lambda x : x[0], reverse = True)
	return ranking[:10]

def logical_or():
	normalize()
	tf_calc()
	idf_calc()
	q = query()
	ranks = rank(q)
	print "Rank    Index    Document"
	for i,r in enumerate(ranks):
		print str(i+1)+"    "+str(r[1])+"    "+content[r[1]]

def logical_and():
	pass

def main():
	logical_or()

if __name__ == '__main__':
	main()
