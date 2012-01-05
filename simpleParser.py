# This file counts the number of words appearances  for each word in a text file
# 
# Siamak Faridani 
# 1/4/2012

# Story:
# I want to find all the rare words in the Biography of Steve Jobs by Isacson 
# This file is the result of that

import csv
import time
import re

stopWords = ('a', 'the', 'an' , 'and', 'of', 'I')
nagationWords = ( 'not' , 'no' , 'don\'t' ,'cannot', 'declined' ,
				'denied' , 'denies' , 'unremarkable', 'without' )


dataset = 'mytextfile' #Change this to point to your own text file

start = time.clock()
print "Starting..."
TextReader = open(dataset +'.txt', 'rb')


rowCounter = 0


for row in TextReader:
	wordCounts = {}
	rowCounter = rowCounter + 1
	
	myText = ''.join(row)
	DocWords =myText.split(" ")
	
	DocWordsCleaned = ""


	for word in DocWords:
		#rules for removing punctuation
		p = re.compile('[^a-zA-Z\']+')
		word = p.sub(' ', word)
		DocWordsCleaned = "".join([DocWordsCleaned, " ", word])
	DocWords = DocWordsCleaned.split(" ")

	prevWord = ""
	for word in DocWords:
		if word in stopWords:
			continue
		#Counting 
		increament = 1
		if prevWord in nagationWords:
			increament = -1
		if word.lower() in wordCounts:
			wordCounts[word.lower()] = wordCounts[word.lower()]+increament
		else:
			wordCounts[word.lower()] =increament
		prevWord = word
	print row, "-->", wordCounts
	print "  "
	print "  "

print " "

elapsed = (time.clock() - start)
print elapsed


