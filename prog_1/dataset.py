#mine
#Email:shruthika62129@gmail.com
import ply.lex as lex
import re
from collections import defaultdict

f = open('Dataset9.txt')
output = []
tweet_output = []
d = defaultdict(int)
tokens = (
		'NUMBER',
		'SNAME',
		'RT',
		'HASHTAG',
		'URL',
		'SLANG',
		'WORD',
		'SINGLEQUOTE',
		'DOUBLEQUOTE',
		'EXCLAMATION',
		'QUESTION',
		'EMOTICON',
		'PUNCTUATION',
		'PERIOD'
		)
t_ignore  = ' \t'

def t_NUMBER(t) :
	r'\d+' 

def t_SNAME(t) :
	r'@\w+'
	d['name'] += 1

def t_HASHTAG(t) :
	r'\#\w+'
	d['hashtag'] += 1

def t_RT(t) :
	r'^RT'
	d['retweet'] += 1
	
def t_URL(t):
	r'https?'
	d['url'] += 1

def t_SLANG(t):
	r'\w+'
	slangs = ['LOL','ROFL','ROFLMAO','DM','ICYMI','CC','NTS','NP','AFAIK','BTW','DP']
	if (t.value).upper() in slangs:
		d['slang'] += 1

def t_EMOTICON(t):
	r'[\:;\-\(\)DPpd]{2,}'
	d['emoticon'] += 1

def t_error(t):
	t.lexer.skip(1)
	
lexer = lex.lex()

for i,line in enumerate(open('Dataset9.txt')):
	line = line.strip()
	if i%2 == 0:
		continue # skip any blank line
	global out
	lexer.input(line)
	lexer.token()
	out = [d['hashtag'], d['retweet'], d['url'], d['name'], d['slang'], d['emoticon']]
	if(d['slang']):
		print line
		print d['slang']
	output.append(out)
	d = defaultdict(int)