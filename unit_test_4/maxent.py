import json
import random
from create_history import get_tuples

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
		self.train_data = []
		self.test_data = []
		self.train_f = []
		self.model = [0 for i in range(10)]
		# self.test_f = []
		
		for i in range(50):
			self.train_data.append(dataset[random.randrange(len(dataset))])
			self.test_data.append(dataset[random.randrange(len(dataset))])
		
		for tup in self.train_data:
			feature_vector = []
			for fun in features:
				feature_vector.append(fun(tup, tup[3]))
			self.train_f.append(feature_vector)
		print self.train_f

	

if __name__ == '__main__':
	MyMaxEnt(get_tuples(), [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10])

		

		