# Remove the K'th element from a list.
#     Example:
#     ?- remove_at(X,[a,b,c,d],2,R).
#     X = b
#     R = [a,c,d]

list1 = ['a','b','c','d']
result1 = []
a = ''

def remove_at_k(x,l1,k,r1):
	x = l1.pop(k-1)
	r1 = l1
	return x,r1

print remove_at_k(a,list1,2,result1)