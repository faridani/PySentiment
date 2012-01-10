# Prepares a zappos dataset to be sent to Weka

import csv
import time
import re
from porterStemmer import StemSentence

dataset = 'allzappostext' #Change this to point to your own text file

def sortedDictValues(adict,i):
	FreqWriter = csv.writer(open('wordFreq.csv', 'w'), delimiter=',', quotechar='"')
	f = open('wordFreq.csv', 'w')
	for wordPair in adict:
		myRow = ''.join([str(wordPair), ",", str(adict[wordPair]),"\n"])
		f.write(myRow)
	return
	f.close()
	

start = time.clock()
print "Starting..."
TextReader = open(dataset +'.txt', 'rb')

wordCounts = {}
rowCounter = 0
documents = []
myText = ""
for row in TextReader:
	rowCounter = rowCounter + 1
	myText = ''.join(StemSentence(row))

	DocWords =myText.split(" ")
	if rowCounter%100 == 0:
		print "Processing line: ", rowCounter
	DocWordsCleaned = ""


	for word in DocWords:
		#rules for removing punctuation
		p = re.compile('[^a-zA-Z\']+')
		word = p.sub(' ', word)
		DocWordsCleaned = "".join([DocWordsCleaned, " ", word])
	DocWords = DocWordsCleaned.split(" ")

	for word in DocWords:
		#Counting 
		if word.lower() in wordCounts:
			wordCounts[word.lower()] = wordCounts[word.lower()]+1
		else:
			wordCounts[word.lower()] =1

sortedDictValues(wordCounts, rowCounter)
elapsed = (time.clock() - start)
print elapsed

#print wordCounts.keys()

wordKeys = wordCounts.keys()
stopWords = ('a', 'the', 'an' , 'and', 'of', 'I')
nagationWords = ( 'not' , 'no' , 'don\'t' ,'cannot', 'declined' ,
				'denied' , 'denies' , 'unremarkable', 'without' )


dataset = 'mytextfile' #Change this to point to your own text file
TextReader = csv.reader(open('zapposdesc.csv', 'rb'), delimiter=',', quotechar='"')
start = time.clock()
print "Starting... featurization"
#TextReader = open(dataset +'.txt', 'rb')


rowCounter = 0

f = open("featres.csv", "w")
for row in TextReader:
	#print row[0]
	wordCounts = [0]*len(wordKeys)
	rowCounter = rowCounter + 1
	row = (row[0])
	myText = ''.join(StemSentence(row))
	#print myText
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
		
		try:
			wordIndex = wordKeys.index(word.lower())
			wordCounts[wordIndex] = wordCounts[wordIndex]+increament
		except:
			print word.lower()
			print row[0]
		prevWord = word
	#print StemSentence(row), "-->", wordCounts
	#print "  "
	#print "  "
	f.write(','.join(str(wordCounts)))
	f.write('\n')

print " "
f.close()

elapsed = (time.clock() - start)
print elapsed


