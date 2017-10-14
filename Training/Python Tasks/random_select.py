# Extract a given number of randomly selected elements from a list.
#     The selected items shall be put into a result list.
#     Example:
#     ?- rnd_select([a,b,c,d,e,f,g,h],3,L).
#     L = [e,d,a]

#     Hint: Use the built-in random number generator random/2 and the result of problem 1.20.
import random

n1 = 3
list1 = ['a','b','c','d','e','f','g','h']
result1 = []

def rnd_select(l1,n,r1):
	r1 = []
	for x in range(n):
		n2 = random.randrange(n)
		r1.append(l1.pop(n2))
	return r1


print rnd_select(list1,n1,result1)