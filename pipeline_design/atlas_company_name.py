"""
Author: Manav Gurnani

	Overall design: Data Processing Pipeline (Company Name Availability)
	1. Data I/O (to build)
		a. Input: parse through tokens using a delimeter
		b. Output: generate output through tokens and delimeter
	2. Name Availability Check System
		a. HashSet to store current names being entered
		b. Normalization conversion function
"""

entries = set()

# SEMI-WORKING STAGE (needs handling for edge cases)
def inputProcessor(inputString, delimeter):
	parsedList = []
	l = 0
	# edge case if delimeter is longer than string size
	if len(delimeter) > len(inputString):
		return []
	# iterating through input with sliding window size of delim
	for i in range(len(inputString)-len(delimeter)):
		if (inputString[i:i+len(delimeter)] == delimeter):
			parsedList.append(inputString[l:i])
			l = i+len(delimeter)
		elif (i == len(inputString)-len(delimeter)-1): # case to check if we're at the end
			parsedList.append(inputString[l:])
			l = i+len(delimeter)
	return parsedList

# WORKING AND TESTED
def outputProcessor(tokenList, delimeter):
	retString = ""
	if tokenList == []:
		return retString
	# iterating up to penultimate elemtn
	for i in range(len(tokenList)-1):
		retString += (tokenList[i] + delimeter)
	retString += tokenList[-1]
	return retString

def removePrefix(inString, invalidArticles):
	return inString

def normalizedString(inString, invalidSuffixes, invalidPrefixes):
	modString = "" # ignoring case
	firstSpace = 1
	inString = inString.lower()
	modString = inString.replace("&", " ")
	modString = modString.replace(",", " ")

	# trying to strip whitespace
	retString = ""
	for i in range(len(modString)):
		if modString[i] == " " and firstSpace:
			retString += '%'
			firstSpace = 0
			continue
		
		elif modString[i] != " " and not firstSpace:
			firstSpace = 1
		
		retString += modString[i]

	retString = retString.replace(" ","")
	retString = retString.replace("%"," ")

	for suffix in invalidSuffixes:
		retString = retString.removesuffix(suffix)
	
	for prefix in invalidPrefixes:
		if retString[0:len(prefix)+1] == (prefix + " "):
			retString = retString[len(prefix)+1:]
			break

	return retString.strip()

def normalizationVerifier(normalizedString):
	if normalizedString.strip() == "":
		return False
	
	return True

def nameCheckOrchestrator(inStrings, invalidSuffixes, invalidPrefixes):
	invalidPrefixes.append("And")

	invalidSuffixes = [suffix.lower() for suffix in invalidSuffixes]
	invalidPrefixes = [prefix.lower() for prefix in invalidPrefixes]

	initAnd = 0

	for name in inStrings:
		if "And " == name[:4]:
			initAnd = 1
		parsed = inputProcessor(name," | ")
		normalized = normalizedString(parsed[1], invalidSuffixes, invalidPrefixes)
		
		if normalizationVerifier(normalized):
			if normalized in entries:
				output = outputProcessor([parsed[0], "Name Not Available"], " | ")
				print(output)
				continue
			else:
				output = outputProcessor([parsed[0], "Name Available"], " | ")
				print(output)
				entries.add(normalized)
		else:
			output = outputProcessor([parsed[0], "Name Not Available"], " | ")
			print(output)

test_names = [
	"1 | The Llama, Inc.",
	"2 | llama inc",
	"3 | Llama & Friends LLC",
	"4 | Llama Friends",
	"5 | A Zebra Corp.",
	"6 | Zebra",
	"7 | And Marble LLC",
	"8 | Marble LLC"
]

nameCheckOrchestrator(test_names,["Inc","Inc.","Corp.","LLC","L.L.C.","LLC."],["The","A","An"])
