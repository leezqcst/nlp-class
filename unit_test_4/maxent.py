import json
import random

def create_dataset():
	f = open("all_data.json")
	json_data = json.load(f)

	history_list = []

	for x in json_data['root']:
	    data = x['data']
	    for y in data:
	        updates = y['updates']
	        for z in range(len(updates)):
	            if (updates[z]['tag'] == 'Model'):
	                updates[z]['tag'] = 'Family'
	            if (updates[z]['tag'] != 'Family' or updates[z]['tag'] != 'Org'):
	                updates[z]['tag'] = 'Other'

	            if (z == 0):
	                history_list.append([None, None, updates[z]['word'], z])
	            elif (z == 1):
	                history_list.append([None, updates[z -1]['tag'], updates[z]['word'], z])
	            else:
	                history_list.append([updates[z - 2]['tag'], updates[z - 1]['tag'], updates[z]['word'], z])
	return history_list

def f1(x,y):
	return random.randrange(2)

def f2(x,y):
	return random.randrange(2)

def f3(x,y):
	return random.randrange(2)

def f4(x,y):
	return random.randrange(2)

def f5(x,y):
	return random.randrange(2)

def f6(x,y):
	return random.randrange(2)

def f7(x,y):
	return random.randrange(2)

def f8(x,y):
	return random.randrange(2)

def f9(x,y):
	return random.randrange(2)

def f10(x,y):
	return random.randrange(2)




class MyMaxEnt(object):
	"""docstring for MyMaxEnt"""
	def __init__(self, dataset, features):
		super(MyMaxEnt, self).__init__()
		self.train = []
		self.test = []
		for i in range(50):
			self.train.append(dataset[random.randrange(len(dataset))])
			self.test.append(dataset[random.randrange(len(dataset))])
		# print self.train
		# print self.test
		print dataset

if __name__ == '__main__':
	MyMaxEnt(create_dataset())

		

		