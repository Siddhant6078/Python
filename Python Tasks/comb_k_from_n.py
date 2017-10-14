# Generate the combinations of K distinct objects chosen from the N elements of a list
#	In how many ways can a committee of 3 be chosen from a group of 12 people? 
# 	We all know that there are C(12,3) = 220 possibilities (C(N,K) denotes the well-known binomial coefficients).
# 	For pure mathematicians, this result may be great.
#	But we want to really generate all the possibilities (via backtracking).

#     Example:
#     ?- combination(3,[a,b,c,d,e,f],L).
#     L = [a,b,c] ;
#     L = [a,b,d] ;
#     L = [a,b,e] ;
import random

list1 = ['a','b','c','d','e','f']
num1 = 3
result1 = []

def perm(n, i,r1):
	r1 = []
	for x in range(i):
		n2 = random.randrange(i)
		r1.append(n.pop(n2))
	r1 = sorted(r1)
	j = 0

	def perm2(r1,j):
		if len(r1) == j:
			print r1
		else:
			for x in xrange(j,len(r1)):
				r1[j], r1[x] = r1[x], r1[j]
				perm2(r1, j + 1)
				r1[j], r1[x] = r1[x], r1[j] # swap back, for the next loop
	perm2(r1,j)

print perm(list1, num1,result1)