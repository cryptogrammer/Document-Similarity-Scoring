import string, math, numpy, sys

#################### TF-IDF portion  ##########################
fileList=[]
for file in range(1,len(sys.argv)):
	fileList.append(sys.argv[file])

def dotProduct(d1,d2):
	answer=0
	for i in range(0, len(d1)):
		answer  = answer + d1[i]*d2[i]
	return(answer)

def vectorMag(d1):
	answer=0
	for x in d1:
		answer = answer + math.pow(x,2)
	return math.sqrt(answer) 

def cosine(d1, d2):
	return dotProduct(d1,d2)/(vectorMag(d1)*vectorMag(d2))

def leaveOutOneCrossValidation(documentVectors):
	part1_answer = {}
	for x in documentVectors.keys():
		currentCosine=0
		best=0
		d1 = x
		d2 = ""
		for y in documentVectors.keys():
			if(y != x):
				currentCosine = cosine(documentVectors[x],documentVectors[y])
				if(currentCosine > best):
					best = currentCosine
					d2 = y
		part1_answer[x] = (d2, best)
	print("filename, "),
	print("match, "),
	print("cosine")
	for x in part1_answer.keys():
		print(x),
		print(", "),
		print(part1_answer[x][0]),
		print(", "),
		print(part1_answer[x][1])

def main():
	uniqueWords=0
	masterDictionary = {}
	unique=[]
	for item in fileList:
		masterDictionary[item] = compute(item)
	N = len(fileList)
	idf_counter = {}
	for file in masterDictionary.keys():
		for word in masterDictionary[file].keys():
			if(not word in unique):
					unique.append(word)
					uniqueWords=uniqueWords+1
	for word in unique:
		idf_counter[word]=0
		for file in fileList:
			if(word in masterDictionary[file].keys()):
				idf_counter[word] = idf_counter[word]+1

	# Definition of idf(t,D)
	# The value of inverse document frequency for term t in document set D is defined as follows:
	# let N be the number of documents, i.e., |D|
	# let count be the number of documents term t appears in (ranges from 1 to N)
	# idf(t,D) = log(N/count)
	for m in idf_counter.keys():
		idf_counter[m] = math.log(float(N)/idf_counter[m])
	for file in masterDictionary.keys():
		for word in masterDictionary[file].keys():
			masterDictionary[file][word] = tf(word,file)*idf_counter[word]

	# to make files ordered in 1, 2, 3...
	posCheck = []
	for file in masterDictionary.keys():
		posCheck.append(file)
	posCheck= sorted(posCheck)
	
	# array with words mapped to their tfidf values for every file
	finalArray = numpy.zeros((uniqueWords,N))
	dictCount=-1
	for item in unique:
		dictCount = dictCount+1
		fileCount=0
		for file in masterDictionary.keys():
			fileCount = posCheck.index(file)
			for word in masterDictionary[file].keys():
				if(word==item):
					finalArray[dictCount][fileCount] = masterDictionary[file][word]
	
	# Putting output in Arrays to use in Project_1C, Part A
	documentVectorsAll={}
	for doc in posCheck:
		documentVectorsAll[doc] = []
 	for row in finalArray:
 		for element in range(0,len(row)):
 			documentVectorsAll[posCheck[element]].append(row[element])
 	leaveOutOneCrossValidation(documentVectorsAll)

# Helper function
# opens file, makes a dictionary of words in the file mapped
# to their frequency in the file.

def compute(fileString):
	file = open(fileString,"r")
	inputString = file.read()
	inputString = str(unicode(inputString, 'ascii', 'ignore'))
	wordCount = {}
	#print((inputString.lower()).translate(None, (string.punctuation+"0123456789")))
	for x in ((inputString.lower()).translate(None, (string.punctuation+"0123456789"))).split():
			if(wordCount.has_key(x)):
				wordCount[x] = wordCount[x]+1
			else:
				wordCount[x] = 1
	return wordCount

# tf for word t in document d
# Definition of tf(t,d)
# The value of term frequency for term t in document d is defined as follows:
# let count_t be the number of times t occurs in document d
# let max_w be the maximum number of times any word occurs in document d
# tf(t,d) = count_t / max_w

def tf(t,d):
	wordCount = compute(d)
	max_w = max(wordCount.values())
	return wordCount[t]/float(max_w)
main()







