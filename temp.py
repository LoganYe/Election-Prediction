#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import os
import re

def str_pre_process(str):
	# remove '\n' first
	str = str.replace("\n"," ")
	# remove url
	str = re.sub(r"http://[a-zA-Z0-9-\./]* ", " ", str)
	str = re.sub(r"http://[a-zA-Z0-9-\./]*$", " ", str)
	str = re.sub(r"https://[a-zA-Z0-9-\./]* ", " ", str)
	str = re.sub(r"https://[a-zA-Z0-9-\./]*$", " ", str)
	# remove special character
	str = re.sub(r"[,-]", " ", str)
	str = re.sub(r"\'s ", " ", str)
	str = re.sub(r"[\(\)\_\'\"\#]", " ", str)
	# remove "..."
	str = re.sub(r"\.\.\.", " ", str)
	# remove "."
	str = re.sub(r"( \.|\. ) ", " ", str)
	# remove "." in the end
	str = re.sub(r"\.$", " ", str)
	# remove ":"
	str = re.sub(r": ", " ", str)
	# remove extra space
	str = re.sub(r" +", " ", str)
	# remove tab
	str = re.sub(r"\t ", " ", str)
	# remove space in head or tail
	str = str.strip()

	return str

stops =["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]	
stops += ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "rt", "co", "se", "html", "http", "https", " ",""]

i = 1
temp = ""

consumer_key = 'FvsE6GQg2cqWOJHQiZaBis4tx'
consumer_secret = 'hcaBUpWWrTCRCrPg79mvdVDCFfwZIkqzb8Cu7Plw38ulJCyQUU'
access_token = '369511457-Y6vRJgXMstv1cDqP3H7XpTbvihjVt0Iqc53ExB7f'
access_secret = '7jH539QYqlGEVdR2jr4h4u36AqCujxQPPREzeDxeWmJ1y'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='voteforsanders', since='2016-01-01', until='2016-04-01').items():	
	if tweet.text == temp:
		continue

	temp = tweet.text
	text_file = open("/Users/Helicopter/Desktop/election_twitters/sanders/sanders"+str(i)+".txt", "w")
	content = str_pre_process(tweet.text)
	for word in content.split():
		word = re.sub("[^a-zA-Z]", "", word)
		if word not in stops:
			print word,
			text_file.write("%s " %word)
	text_file.close()
	i += 1

for tweet in tweepy.Cursor(api.search, q='feelthebern', since='2016-01-01', until='2016-04-01').items():	
	if tweet.text == temp:
		continue

	temp = tweet.text
	text_file = open("/Users/Helicopter/Desktop/election_twitters/sanders/sanders"+str(i)+".txt", "w")
	content = str_pre_process(tweet.text)
	for word in content.split():
		word = re.sub("[^a-zA-Z]", "", word)
		if word not in stops:
			print word,
			text_file.write("%s " %word)
	text_file.close()
	i += 1





