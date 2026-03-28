"""
Author: Manav Gurnani

Problem: String Subsequences
Description: Given a string s and a 2-letter string t, count the number of subsequences of s that equal t. 
"""

from collections import defaultdict

# Concept: Need to traverse string from left to right. As we traverse it, we must maintain a record of all the characters we've seen thus far.
# While we maintain a record, we look to see if we find the second character. When we do, we check to see how many occurrences of the first character we've seen (and add it).

def findSubsequences(s: str, t: str) -> int:
	character_directory = defaultdict(int)

	if s == "":
		return 0

	num_subsequences = 0

	for i in range(len(s)):
		if s[i] == t[1]: # if second element
			num_subsequences += character_directory[t[0]]
		character_directory[s[i]] += 1
	return num_subsequences

print(findSubsequences("xaxbxbx","ab"))

# TIME TO SOLVE: ~20 minutes
