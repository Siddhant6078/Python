# Decode a run-length encoded list of encode_modified file.
# Given a run-length code list generated as specified in problem 1.11.
# Construct its uncompressed version.

from itertools import groupby

b = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
count_dups = [[sum(1 for i in g),k] for k,g in groupby(b)]
# print(count_dups)
# Output: [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]

# my_list1 = []
# my_list2 = []
my_list = []

for x in count_dups:
	my_list1.append(x[::2])
	my_list2.append(x[1::2])

for x in my_list1:
	for j in range(len(my_list1)):
		for y in range(x[j]):
			# my_list.append(my_list2[j])
			print my_list2[j]		

print my_list
print my_list1 # [[4], [1], [2], [2], [1], [4]]
print my_list2 # [['a'], ['b'], ['c'], ['a'], ['d'], ['e']]

