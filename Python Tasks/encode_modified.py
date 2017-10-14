# 1.11 (*) 	Modified run-length encoding.
# Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

# Example:
# ?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
# X = [[4,a],b,[2,c],[2,a],[1,d],[4,e]]

# from itertools import groupby

list1 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
result1 = []
# count_dups = [[sum(1 for i in g),k] for k,g in groupby(b)]
# print(count_dups)
# Output: [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]

def encode_modified(l1,r1):
	r1 = []
	current = l1[0]
	count = 0
	for value in l1:
	    if value == current:
	        count += 1
	    else:
	        r1.append([count,current])
	        current = value
	        count = 1
	r1.append([count,current])
	return r1

print encode_modified(list1,result1)