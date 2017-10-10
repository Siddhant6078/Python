# 1.11 (*) 	Modified run-length encoding.
# Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

# Example:
# ?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
# X = [[4,a],b,[2,c],[2,a],[1,d],[4,e]]

from itertools import groupby

b = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
count_dups = [[sum(1 for i in g),k] for k,g in groupby(b)]
print(count_dups)
# Output: [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]