import re
from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

fp = open("cri.txt")
content = eval(fp.read())
docs = []
processed_docs = []
stemmer = PorterStemmer()

def remove_stop_words_punctuation():
	stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'between', 'into','to', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'in', 'on', 'under', 'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor',  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
	punctuation = [',', '.', '?', '!']
	for doc in content:
		doc = re.sub(r'(,)([0-9]+)', r"\1 \2", doc)
		doc = wt(doc)
		sentence = []
		for word in doc:
			if word not in stop and word not in punctuation:
				sentence.append(stemmer.stem(word))
		processed_docs.append(sentence)

def main():
	remove_stop_words_punctuation()
	print processed_docs

if __name__ == '__main__':
	main()
