# Decode a run-length encoded list of encode_modified file.
# Given a run-length code list generated as specified in problem 1.11.
# Construct its uncompressed version.

# Input: [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
# Output: ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']

input1 = [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
str1 = []

def decode_modified(l1,r1):
	for x in l1:
		for y in range(x[0]):
			r1.append(x[1])
	return r1

print decode_modified(input1,str1)