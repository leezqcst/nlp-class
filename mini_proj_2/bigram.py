import nltk
<<<<<<< HEAD

from nltk.corpus import brown

# an nltk.FreqDist() is like a dictionary,
# but it is ordered by frequency.
# Also, nltk automatically fills the dictionary
# with counts when given a list of words.

freq_brown = nltk.FreqDist(brown.words())

freq_brown.keys()
freq_brown.items()[:20]

# an nltk.ConditionalFreqDist() counts frequencies of pairs.
# When given a list of bigrams, it maps each first word of a bigram
# to a FreqDist over the second words of the bigram.

cfreq_brown_2gram = nltk.ConditionalFreqDist(nltk.bigrams(brown.words()))

# conditions() in a ConditionalFreqDist are like keys()
# in a dictionary

cfreq_brown_2gram.conditions()

# the cfreq_brown_2gram entry for "my" is a FreqDist.

cfreq_brown_2gram["my"]

# here are the words that can follow after "my".
# We first access the FreqDist associated with "my",
# then the keys in that FreqDist

cfreq_brown_2gram["my"].keys()

# here are the 20 most frequent words to come after "my", with their frequencies

cfreq_brown_2gram["my"].items()[:20]

# an nltk.ConditionalProbDist() maps pairs to probabilities.
# One way in which we can do this is by using Maximum Likelihood Estimation (MLE)

cprob_brown_2gram = nltk.ConditionalProbDist(cfreq_brown_2gram, nltk.MLEProbDist)

# This again has conditions() wihch are like dictionary keys

cprob_brown_2gram.conditions()

# Here is what we find for "my": a Maximum Likelihood Estimation-based probability distribution,
# as a MLEProbDist object.

cprob_brown_2gram["my"]

# We can find the words that can come after "my" by using the function samples()

cprob_brown_2gram["my"].samples()

# Here is the probability of a particular pair:

cprob_brown_2gram["my"].prob("own")

# and we can draw a random word to follow "my"
# based on the probabilities of the bigrams

cprob_brown_2gram["my"].generate()

# We can use this to generate text at random
# based on a given text of bigrams.
# Let's do this for the Sam "corpus"

corpus = """<s> I am Sam </s>
<s> Sam I am </s>
<s> I do not like green eggs and ham </s>"""

words = corpus.split()
cfreq_sam = nltk.ConditionalFreqDist(nltk.bigrams(words))
cprob_sam = nltk.ConditionalProbDist(cfreq_sam, nltk.MLEProbDist)

word = "<s>"
for index in range(50):
    word = cprob_sam[ word].generate()
    print word,
print

# Not a lot of variety. We need a bigger corpus.
# What kind of genres do we have in the Brown corpus?
brown.categories()    

# Let's try Science Fiction.
cfreq_scifi = nltk.ConditionalFreqDist(nltk.bigrams(brown.words(categories = "science_fiction")))
cprob_scifi = nltk.ConditionalProbDist(cfreq_scifi, nltk.MLEProbDist)

word = "in"
for index in range(50):
    word = cprob_scifi[ word ].generate()
    print word,
print

# try this with other Brown corpus categories.

# For the nltk.book objects, there is a generate() function.
from nltk.book import *
text6.generate()
text7.generate()
text2.generate()

# Do you think they used bigrams like we did earlier, or some larger n-grams?
=======
from math import log
from collections import defaultdict
import re
words = nltk.word_tokenize("~ "+open("corpus2.txt").read().lower()+" ~")
count = defaultdict(int)
count_bigram = defaultdict(int)

cleaned_words = []
punctuation = [',', '.', '?', '!', ':', ';', '\'', '\"','@', '=', '&', '(', ')' ,'[', ']']
for word in words:
	if(not (word in punctuation)):
		word = re.sub(r'[,.\'`]','',word)
		if(len(word) > 0):
			cleaned_words.append(word)
			count[word] += 1

for i in range(len(cleaned_words)-1):
	count_bigram[(cleaned_words[i],cleaned_words[i+1])] += 1

for key,value in count_bigram.iteritems():
	q_ML = float(value)/count[key[0]]
	print key[0]+","+key[1]+","+str(q_ML)+","+str(log(q_ML))

>>>>>>> d4de9b21ef3077a92fb0fab67dcadaeeb2bf0292
