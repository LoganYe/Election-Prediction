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

#######################################################
#                  TRUMP

consumer_key = 'WxTe8yfQSLryHW8y3opcUqLaf'
consumer_secret = 'VCRTiuIVIygQdSv2TkXkIE9mjOWtZV2yt5LG4i4ezAxKDdNZIN'
access_token = '4861285741-REyJElpNwqgyYVwAjk7ZUqk2COJCQ6a6aRXhKao'
access_secret = 'SFwXgR4LD1borLckFb2darrUszjMP7v3wjtk1q7bB3ynT'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

text_file = open("/Users/Helicopter/Desktop/election_twitters/Output_trump.txt", "w")
for tweet in tweepy.Cursor(api.search, q='votefortrump', since='2016-03-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)

consumer_key = 'ArXdgVEiWGTTUH8fPz1zypTTY'
consumer_secret = 'NHP1yRDoD3x6HznLAKLevE70wEuSw7FVQL6Lg2PSI3LvgeFTK5'
access_token = '4836303139-iZuj2DRjnN1QeT3oRrNTG9FH9sVlSsF68V7LtyU'
access_secret = 'S9h3I2dM9j4pbhex7F2lkwpD6js70YjEsxbA9DKl5oOOL'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='trumpnation', since='2016-03-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)

consumer_key = 'VqOrvXICD2HXETkeM9gDnEOFB'
consumer_secret = 'p25tQ8k3A12JBUyWiKppk8KJl65Fd3vED3eIlobbIJKSONL6a7'
access_token = '4836303139-uBPK54GipQWCy8X4ruIdOC5jbPfpu1bU4DGOoSE'
access_secret = 'TRFKoEQhOX2dO7enOUeoXHbw9PPTsIioR0GDFqksa9bFO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='teamtrump', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)

text_file.close()

#######################################################
#                  CRUZ

consumer_key = 'FvsE6GQg2cqWOJHQiZaBis4tx'
consumer_secret = 'hcaBUpWWrTCRCrPg79mvdVDCFfwZIkqzb8Cu7Plw38ulJCyQUU'
access_token = '369511457-Y6vRJgXMstv1cDqP3H7XpTbvihjVt0Iqc53ExB7f'
access_secret = '7jH539QYqlGEVdR2jr4h4u36AqCujxQPPREzeDxeWmJ1y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

text_file = open("/Users/Helicopter/Desktop/election_twitters/Output_cruz.txt", "w")
for tweet in tweepy.Cursor(api.search, q='voteforcruz', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='onlycruz', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='choosecruz', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='cruzcrew', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='cruz2016', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='unitedwithted', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='trusted', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='cruztovictory', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)

text_file.close()

#######################################################
#                  CLINTON

consumer_key = 'xWJoX2wcnl2wSTjOIz4DVPQwT'
consumer_secret = 'MSxpYuyUy2xXyEK61ljwZrwDeDrSErTNNuzhx6F3Peb8TbbCzt'
access_token = '2739558996-HQOgiy3LHivAeN7z9QWLBNedmpn5KmWQFz8t4SR'
access_secret = '2abrCehxSKixtQe3qBTivrazHeRJuZJQTGr0xeFiMrvmh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

text_file = open("/Users/Helicopter/Desktop/election_twitters/Output_clinton.txt", "w")
for tweet in tweepy.Cursor(api.search, q='voteforclinton', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='voteforhillary', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='hillaryforpresident', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='hillary2016', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='clinton2016', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='vote4hillary', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='teamclinton', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)			
for tweet in tweepy.Cursor(api.search, q='vote4clinton', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)
for tweet in tweepy.Cursor(api.search, q='standwithhillary', since='2016-01-01', until='2016-04-01').items():
	content = str_pre_process(tweet.text)
	for word in content.split():
		letters_only = re.sub("[^a-zA-Z]", "", word)
		word = letters_only.lower()
		if word not in stops:
			print word,
			text_file.write("%s " %word)

text_file.close()


