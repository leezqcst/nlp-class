'''
MyMaxEnt.py
MaxEnt Classifier
Author: Anantharaman Narayana Iyer
Date: 21 Nov 2014
'''
import json
import numpy
import math
import pickle
from collections import defaultdict

from scipy.optimize import minimize as mymin 
import datetime

# ----------------------------------------------------------------------------------------
# maxent implementation
# ----------------------------------------------------------------------------------------
class MyMaxEnt(object):
    def __init__(self, history_tuples, function_obj, reg_lambda = 0.01, pic_file = None): 
        # history_tuples is of the form: ((ta, tb, wn, i), tag) where ta = tag t-2, tb = tag t-1, wn = pointer to a sentence, i = current index
        # function_list is of the form: [(pointer_to_function_f1, tag_for_f1), (pointer_to_function_f2, tag_for_f2)...]
        # reg_lambda = regularization coefficient
        # pic_file = Name of file where the classifier is pickled
        self.h_tuples = history_tuples
        self.func = function_obj
        self.reg = reg_lambda
        self.dataset = None # this will be set by create_dataset
        self.tag_set = self.func.supported_tags #None # this will be also be set by create_dataset - this is the set of all tags
        self.create_dataset()
        self.dim = self.dataset.shape[1] #len(self.dataset[0])
        self.num_examples = self.dataset.shape[0]
        self.model = numpy.array([0 for d in range(self.dim)]) # initialize the model to all 0
        self.pic_file = pic_file
        return

    def create_dataset(self):
        self.dataset = []
        self.all_data = {}
        for h in self.h_tuples[:9000]: # h represents each example x that we will convert to f(x, y)
            for tag in self.tag_set:
                feats = self.all_data.get(tag, [])
                val = self.get_feats(h[0], tag)
                feats.append(val)
                self.all_data[tag] = feats
                if (h[1] == tag):
                    self.dataset.append(val)
        for k, v in self.all_data.items():
            self.all_data[k] = numpy.array(v)
        self.dataset = numpy.array(self.dataset)
        return

        
    def get_feats(self, xi, tag): # xi is the history tuple and tag is y belonging to Y (the set of all labels
        # xi is of the form: history where history is a 4 tuple by itself
        # self.func is the function object
        return self.func.evaluate(xi, tag)

    def train(self):
        dt1 = datetime.datetime.now()                   
        print 'before training: ', dt1         
        params = mymin(self.cost, self.model, method = 'L-BFGS-B') #, jac = self.gradient) # , options = {'maxiter':100}
        self.model = params.x
        dt2 = datetime.datetime.now()
        print 'after training: ', dt2, '  total time = ', (dt2 - dt1).total_seconds()
        
        if self.pic_file != None:
            pickle.dump(self.model, open(self.pic_file, "wb"))
        return

    def p_y_given_x(self, xi, tag): # given xi determine the probability of y - note: we have all the f(x, y) values for all y in the dataset
        normalizer = 0.0
        feat = self.get_feats(xi, tag)
        dot_vector = numpy.dot(numpy.array(feat), self.model)
        for t in self.tag_set:
            feat = self.get_feats(xi, t)
            dp = numpy.dot(numpy.array(feat), self.model)
            if dp == 0:
                normalizer += 1.0
            else:
                normalizer += math.exp(dp)
        if dot_vector == 0:
            val = 1.0
        else:
            val = math.exp(dot_vector) # 
        result = float(val) / normalizer
        return result

    def classify(self, xi):
        if self.pic_file != None:
            self.model = pickle.load(open(self.pic_file, "rb"))
        maxval = 0.0
        result = None
        for t in self.tag_set:
            val = self.p_y_given_x(xi, t)
            if val >= maxval:
                maxval = val
                result = t
        return result

    def cost(self, params):
        self.model = params
        sum_sqr_params = sum([p * p for p in params]) # for regularization
        reg_term = 0.5 * self.reg * sum_sqr_params                
        dot_vector = numpy.dot(self.dataset, self.model)
        
        empirical = numpy.sum(dot_vector) # this is the emperical counts            
        expected = 0.0
        
        for j in range((self.num_examples)):
            mysum = 0.0
            for tag in self.tag_set: # get the jth example feature vector for each tag
                fx_yprime = self.all_data[tag][j] #self.get_feats(self.h_tuples[j][0], tag)
                '''
                dot_prod = 0.0
                for f in range(len(fx_yprime)):
                    if fx_yprime[f] != 0:
                        dot_prod += self.model[f]
                '''
                dot_prod = numpy.dot(fx_yprime, self.model)
                if dot_prod == 0:
                    mysum += 1.0
                else:
                    mysum += math.exp(dot_prod)
            expected += math.log(mysum)
        print "Cost = ", (expected - empirical + reg_term)
        return (expected - empirical + reg_term)

    def gradient(self, params):
        self.model = params        
        gradient = []
        for k in range(self.dim): # vk is a m dimensional vector
            reg_term = self.reg * params[k]
            empirical = 0.0
            expected = 0.0
            for dx in self.dataset:
                empirical += dx[k]
            for i in range(self.num_examples):
                mysum = 0.0 # exp value per example
                for t in self.tag_set: # for each tag compute the exp value
                    fx_yprime = self.all_data[t][i] #self.get_feats(self.h_tuples[i][0], t)

                    # --------------------------------------------------------
                    # computation of p_y_given_x
                    normalizer = 0.0
                    dot_vector = numpy.dot(numpy.array(fx_yprime), self.model)
                    for t1 in self.tag_set:
                        feat = self.all_data[t1][i]
                        dp = numpy.dot(numpy.array(feat), self.model)
                        if dp == 0:
                            normalizer += 1.0
                        else:
                            normalizer += math.exp(dp)
                    if dot_vector == 0:
                        val = 1.0
                    else:
                        val = math.exp(dot_vector) # 
                    prob = float(val) / normalizer
                    # --------------------------------------------------------
                    
                    mysum += prob * float(fx_yprime[k])                    
                expected += mysum
            gradient.append(expected - empirical + reg_term)
        return numpy.array(gradient)
    
    def innerproduct(self, a, b):
        return sum([i+j for i,j in zip(a,b)])

    def loglinear(self, history_tuple, tag):
        num = math.exp(self.innerproduct(self.model, self.func.evaluate(history_tuple, tag)))
        denom = 0.0        
        for tag_x in self.tag_set:
            denom += math.exp(self.innerproduct(self.model, self.func.evaluate(history_tuple, tag_x)))
        return num/denom
    
        
    def r(self, tag_list_k, history_tuples_k):
        prod = 0.0
        for i in range(len(tag_list_k)):
            p = loglinear(history_tuples_k[i], tag_list_k[i])
            prod *= p
        return prod
    
    def genDataStructure(self,n):
        tags_considered = {'OS':0.0,'Version':0.0,'Org':0.0,'Other':0.0}
        combos = {'OS':tags_considered, 'Org':tags_considered,'Version':tags_considered,'Other':tags_considered}
        x = defaultdict(float)
        return [x for i in range(0,n+1)]


    def pi_f(self, k, u, v):
        probabs = []
        for t in self.tag_set:
            probabs.append(pi(k-1, t, u) * loglinear(cur_history_tuple[0], cur_history_tuple[1]))
            
    def viterbi(self, sentence_len, sentence_index):
        pi = self.genDataStructure(sentence_len)
        bp = self.genDataStructure(sentence_len)
        for k in range(1, sentence_len):
            if(k==1):
                tags_t = ['*']
                tags_u = ['*']
                tags_v = self.tag_set
            if(k==2):
                tags_t = ['*']
                tags_u = self.tag_set
                tags_v = self.tag_set
            else:
                tags_t = self.tag_set
                tags_u = self.tag_set
                tags_v = self.tag_set
            for u in tags_u:
                for v in tags_v:
                    probabs = []
                    for t in tags_t:
                        probabs.append(pi[k-1][u][t] * self.loglinear(self.h_tuples[sentence_index+k][0], self.h_tuples[sentence_index+k][1]))
                        pi[k][v][u] = max(probabs)
                        high_p = 0
                    for i,p in enumerate(probabs):
                        if p > high_p:
                            high_p = p
                            bp[k][v][u] = self.tag_set[i]

        print bp
        
        
        
        

if __name__ == "__main__":
    pass
