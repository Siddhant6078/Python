# Rotate a list N places to the left.
#     Examples:
#     ?- rotate([a,b,c,d,e,f,g,h],3,X).
#     X = [d,e,f,g,h,a,b,c]

#     ?- rotate([a,b,c,d,e,f,g,h],-2,X).
#     X = [g,h,a,b,c,d,e,f]

list1 = ['a','b','c','d','e','f','g','h']
result1 = []

def rotate_list_n_left(l1,n,r1):
	r1 = l1
	if n>=0:	
		spl1 = r1[:n]
		for x in spl1:
			r1.remove(x)
			r1.append(x)
		return r1
	else:
		spl1 = r1[:n]
		for x in range(n+1,1,1):
			p1 = r1.pop()
			r1.insert(0,p1)
		return r1

print rotate_list_n_left(list1,-3,result1)