# Drop every N'th element from a list.
#     Example:
#     ?- drop([a,b,c,d,e,f,g,h,i,k],3,X).
#     X = [a,b,d,e,g,h,k]

list1 = ['a','b','c','d','e','f','g','h','i','k']
result1 = []

def drop_n(l1,n,r1):
	r1 = []
	for x in range(len(l1)):
		if x%n == (n-1):
			continue
		else:
			r1.append(l1[x])
	return r1

print drop_n(list1,3,result1)