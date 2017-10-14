# Duplicate the elements of a list.
# 	Example:
# 	?- dupli([a,b,c,c,d],X).
# 	X = [a,a,b,b,c,c,c,c,d,d]
print 'Duplicate each element of list'
list1 = ['a','b','c','c','d']
result1 = []
def duplcate_each(l1,r1):
	for i in l1:
		r1.extend([i, i])
	return r1

print duplcate_each(list1,result1)

# Duplicate the elements of a list.
# 	Example:
# 	?- dupli([a,b,c,d],X).
# 	X = [a,b,b,c,c,c,d,d,d,d]

print 'Print each element of list as per its index number'

list2 = ['a','b','c','d']
result2 = []
def duplcate_index_times(l2,r2):
	for index, item in enumerate(l2):
		for x in range(index+1):
			r2.append(item)
	return r2

print duplcate_index_times(list2,result2)

print 'Duplicate the elements of a list a given number of times.'
# Duplicate the elements of a list a given number of times.
# 	Example:
# 	?- dupli([a,b,c],3,X).
# 	X = [a,a,a,b,b,b,c,c,c]

# 	What are the results of the goal:
# 	?- dupli(X,3,Y).

list3 = ['a','b','c','d']
result3 = []

def duplcate_n_times(l3,n,r3):
	for index, item in enumerate(l3):
		for x in range(n):
			r3.append(item)
	return r3

print duplcate_n_times(list3,4,result3)