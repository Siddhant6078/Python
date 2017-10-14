# Generate a random permutation of the elements of a list.
#     Example:
#     ?- rnd_permu([a,b,c,d,e,f],L).
#     L = [b,a,d,c,e,f]

#     Hint: Use the solution of problem 1.23.
import random

list1 = ['a','b','c','d','e','f']
result1 = []

def rnd_permu(l1,r1):
 	r1 = []
 	n1 = len(l1)
 	rnd = random.sample(range(n1), n1)
	for x in rnd:
		r1.append(l1[x])
	return r1

print rnd_permu(list1,result1)