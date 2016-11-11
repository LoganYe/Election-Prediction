#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import walk
import re
import numpy as np
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

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

def get_model(trump, cruz, kasich, clinton, sanders):
	trainer = Trainer(tokenizer)

	twiSet = []
	for address in trump:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/trump/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
			struct = {'text': content, 'category': 'trump'}
		twiSet.append(struct)
		text_file.close()

	for address in cruz:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/cruz/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
			struct = {'text': content, 'category': 'cruz'}
		twiSet.append(struct)
		text_file.close()

	for address in kasich:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/kasich/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
			struct = {'text': content, 'category': 'kasich'}
		twiSet.append(struct)
		text_file.close()

	for address in clinton:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/clinton/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
			struct = {'text': content, 'category': 'clinton'}
		twiSet.append(struct)
		text_file.close()

	for address in sanders:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/sanders/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
			struct = {'text': content, 'category': 'sanders'}
		twiSet.append(struct)
		text_file.close()

	for twi in twiSet:
		trainer.train(twi['text'], twi['category'])
	
	newclassifier = Classifier(trainer.data, tokenizer)

	return newclassifier

def get_result(model, trump, cruz, kasich, clinton, sanders):

	result = []
	test = []
	for address in trump:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/trump/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
		classification = model.classify(content)
		result.append(classification)
		test.append('trump')
		text_file.close()

	for address in cruz:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/cruz/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
		classification = model.classify(content)
		result.append(classification)
		test.append('cruz')
		text_file.close()

	for address in kasich:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/kasich/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
		classification = model.classify(content)
		result.append(classification)
		test.append('kasich')
		text_file.close()

	for address in clinton:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/clinton/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
		classification = model.classify(content)
		result.append(classification)
		test.append('clinton')
		text_file.close()

	for address in sanders:
		with open("/Users/Helicopter/Desktop/Logan_s/Courses/Stat_AI_ML/election/election_twitters/sanders/" + address,"r") as text_file:	
			content = ""
			for line in text_file:
				for word in line.split():
					content = content + word + " "
		classification = model.classify(content)
		result.append(classification)
		test.append('sanders')
		text_file.close()

	return result, test

def cal_acc(result, test):
	sum = len(test)
	match = 0
	for i in xrange(sum):
		if(result[i][0][0] == test[i]):
			match += 1

	return match*1.0/sum



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
#print "Building Wordbag..."
# No of Words in bag
#bag = wordbag(trump_train, cruz_train, kasich_train, clinton_train, sanders_train)
#print bag

# Training set & Testing set

print "Training..."
model = get_model(trump_train, cruz_train, kasich_train, clinton_train, sanders_train)
#print model

print "Testing..."
#result, test = get_result(model, trump_test, cruz_test, kasich_test, clinton_test, sanders_test)
result = model.classify("gay marriage is great")
#result = model.classify("When you are suffering at night because of acid pain, realizing all your hard work at the gym will be gone after surviving than less one meal per day and go to sleep with hunger and muscle pain knowing your body is metabolizing it for energy ‪#‎MakeDonaldDrumpfAgain‬ Join the Movement! Donald Trump cannot be presdient")
#result = model.classify("I’ll be one of my favorite places this morning, Staten Island. Big crowd, will be fun!")
#result = model.classify("makeamericagreatagain")
#result = model.classify("the wall")
print result
#accuracy = cal_acc(result, test)
#print accuracy
#for item in result:
#	print item[0][0]
#print test




