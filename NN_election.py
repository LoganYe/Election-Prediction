#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import walk
import re
import numpy as np
from sklearn import linear_model, datasets, metrics
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

def wordbag(trump, cruz, kasich, clinton, sanders):

	bag = []
	stops =["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]	
	stops += ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "rt", "co", "se", "html", " ",""]

	for address in trump:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/trump/" + address,"r") as text_file:			
			for line in text_file:
				for word in line.split():
					letters_only = re.sub("[^a-zA-Z]", " ", word)
					word = letters_only.lower()
					if (word not in bag) and (word not in stops):
						bag.append(word)
		text_file.close()
	for address in cruz:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/cruz/" + address,"r") as text_file:			
			for line in text_file:
				for word in line.split():
					letters_only = re.sub("[^a-zA-Z]", " ", word)
					word = letters_only.lower()
					if (word not in bag) and (word not in stops):
						bag.append(word)
		text_file.close()
	for address in kasich:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/kasich/" + address,"r") as text_file:			
			for line in text_file:
				for word in line.split():
					letters_only = re.sub("[^a-zA-Z]", " ", word)
					word = letters_only.lower()
					if (word not in bag) and (word not in stops):
						bag.append(word)
		text_file.close()
	for address in clinton:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/clinton/" + address,"r") as text_file:			
			for line in text_file:
				for word in line.split():
					letters_only = re.sub("[^a-zA-Z]", " ", word)
					word = letters_only.lower()
					if (word not in bag) and (word not in stops):
						bag.append(word)
		text_file.close()
	for address in sanders:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/sanders/" + address,"r") as text_file:			
			for line in text_file:
				for word in line.split():
					letters_only = re.sub("[^a-zA-Z]", " ", word)
					word = letters_only.lower()
					if (word not in bag) and (word not in stops):
						bag.append(word)
		text_file.close()
	
	print len(bag)
	return bag

def get_attr(bag, trump, cruz, kasich, clinton, sanders, flag):
	num_twi = len(trump) + len(cruz) + len(kasich) + len(clinton) + len(sanders)
	num_attr = len(bag)
	X = np.zeros((num_twi, num_attr))
	Y = np.zeros(num_twi)
	i = 0				# index of twitter
	if flag == 0:
		folder = "election_twitters"
	else:
		folder = "test_twitters"

	for address in trump:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/" + folder + "/trump/" + address,"r") as text_file:		
			j = 0		# index of attributes
			word_dict = dict.fromkeys(bag,0)
			for line in text_file:
				for word in line.split():
					if word in bag:
						word_dict[word] += 1
		for key in word_dict:
			X[i, j] = word_dict[key]
			j += 1
		Y[i] = 1
		text_file.close()
		i += 1

	for address in cruz:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/" + folder + "/cruz/" + address,"r") as text_file:			
			j = 0		# index of attributes
			word_dict = dict.fromkeys(bag,0)
			for line in text_file:
				for word in line.split():
					if word in bag:
						word_dict[word] += 1
		for key in word_dict:
			X[i, j] = word_dict[key]
			j += 1
		Y[i] = 2
		text_file.close()
		i += 1

	for address in kasich:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/" + folder + "/kasich/" + address,"r") as text_file:			
			j = 0		# index of attributes
			word_dict = dict.fromkeys(bag,0)
			for line in text_file:
				for word in line.split():
					if word in bag:
						word_dict[word] += 1
		for key in word_dict:
			X[i, j] = word_dict[key]
			j += 1
		Y[i] = 3
		text_file.close()
		i += 1

	for address in clinton:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/" + folder + "/clinton/" + address,"r") as text_file:			
			j = 0		# index of attributes
			word_dict = dict.fromkeys(bag,0)
			for line in text_file:
				for word in line.split():
					if word in bag:
						word_dict[word] += 1
		for key in word_dict:
			X[i, j] = word_dict[key]
			j += 1
		Y[i] = 4
		text_file.close()
		i += 1

	for address in sanders:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/" + folder + "/sanders/" + address,"r") as text_file:			
			j = 0		# index of attributes
			word_dict = dict.fromkeys(bag,0)
			for line in text_file:
				for word in line.split():
					if word in bag:
						word_dict[word] += 1
		for key in word_dict:
			X[i, j] = word_dict[key]
			j += 1
		Y[i] = 5
		text_file.close()
		i += 1

	return X, Y

trump_train = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/trump"):
    trump_train.extend(filenames)
    break
cruz_train = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/cruz"):
    cruz_train.extend(filenames)
    break
kasich_train = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/kasich"):
    kasich_train.extend(filenames)
    break
clinton_train = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/clinton"):
    clinton_train.extend(filenames)
    break
sanders_train = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/sanders"):
    sanders_train.extend(filenames)
    break

trump_test = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/test_twitters/trump"):
    trump_test.extend(filenames)
    break
cruz_test = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/test_twitters/cruz"):
    cruz_test.extend(filenames)
    break
kasich_test = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/test_twitters/kasich"):
    kasich_test.extend(filenames)
    break
clinton_test = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/test_twitters/clinton"):
    clinton_test.extend(filenames)
    break
sanders_test = []
for (dirpath, dirnames, filenames) in walk("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/test_twitters/sanders"):
    sanders_test.extend(filenames)
    break


#Main
print "BUILDING WORDBAG..."
# No of Words in bag
bag = wordbag(trump_train, cruz_train, kasich_train, clinton_train, sanders_train)
#print bag
print "BUILDING MATRIX..."

# Training set & Testing set
X_train, Y_train = get_attr(bag, trump_train, cruz_train, kasich_train, clinton_train, sanders_train, 0)
X_test, Y_test = get_attr(bag, trump_test, cruz_test, kasich_test, clinton_test, sanders_test, 1)
##
#print X_train
#print Y_train
#print len(X_train), len(Y_train)

print "TRAINING..."

logistic = linear_model.LogisticRegression()
rbm = BernoulliRBM(random_state=0, verbose=True)

classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])

# Hyper-parameters. These were set by cross-validation,
# using a GridSearchCV. Here we are not performing cross-validation to
# save time.
rbm.learning_rate = 0.06
rbm.n_iter = 10
# More components tend to give better prediction performance, but larger
# fitting time
rbm.n_components = 50
logistic.C = 6000.0

# Training RBM-Logistic Pipeline
classifier.fit(X_train, Y_train)

# Training Logistic regression
logistic_classifier = linear_model.LogisticRegression(C=100.0)
logistic_classifier.fit(X_train, Y_train)

####################### Testing ############################

print()
print("Logistic regression using RBM features:\n%s\n" % (
    metrics.classification_report(
        Y_test,
        classifier.predict(X_test))))

print("Logistic regression using raw pixel features:\n%s\n" % (
    metrics.classification_report(
        Y_test,
        logistic_classifier.predict(X_test))))
