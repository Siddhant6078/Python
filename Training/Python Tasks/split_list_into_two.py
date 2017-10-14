 # Split a list into two parts; the length of the first part is given.
 #    Do not use any predefined predicates.

 #    Example:
 #    ?- split([a,b,c,d,e,f,g,h,i,k],3,L1,L2).
 #    L1 = [a,b,c]
 #    L2 = [d,e,f,g,h,i,k]

list1 = ['a','b','c','d','e','f','g','h','i','k']
list2 = []
list3 = []

def split_into_two(l1,n,l2,l3):
	l2 = []
	l3 = []
	for x in range(len(l1)):
		if x<n:
			l2.append(l1[x])
		else:
			l3.append(l1[x])
	return l2,l3

print split_into_two(list1,4,list2,list3)