import json
from collections import defaultdict

trees = []
counts = defaultdict(int)
new_terminals = []
fp = open('train_rare','w')


def tree_iterate(tree):
	for each in tree:
		if(isinstance(each,unicode)):
			counts[each] += 1
		else:
			tree_iterate(each)

def check_rare():
	for key,value in counts.iteritems():
		if value > 5:
			new_terminals.append(key)

def tree_replace(tree):
	for each in tree:
		if(isinstance(each[-1],list)):
			if(each[-1] not in new_terminals):
				each[-1] = u'_RARE_'
	json.dump(tree, fp)
	fp.write('\n')

def tree_replace_v2(tree):
	for each in tree:
		if(isinstance(each[-1],list)):
			tree_replace_v2(each)
		elif(isinstance(each[-1],unicode)):
			if(each[-1] not in new_terminals):
				print type(each)
				#each[-1] = '_RARE_'
	json.dump(tree, fp)
	fp.write('\n')			

def tree_replace_v3(tree):
	#print list(map(lambda x:isinstance(x,unicode),tree))
	#print reduce(lambda x,y:x and y,list(map(lambda x:isinstance(x,unicode),tree)))
	if(reduce(lambda x,y:x and y,list(map(lambda x:isinstance(x,unicode),tree)))):
	 	if(tree[-1] not in new_terminals):
	 		tree[-1] = '_RARE_'
	for each in tree:
		if(isinstance(each,list)):
			tree_replace_v3(each)
	json.dump(tree, fp)
	fp.write('\n')


if __name__ == '__main__':
	with open('parse_train.dat') as openfile:
		for line in openfile:
			tree = json.loads(line)
			tree_iterate(tree)
			trees.append(tree)
	check_rare()
	for tree in trees:
		tree_replace_v3(tree)
