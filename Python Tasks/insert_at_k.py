# Insert an element at a given position into a list.
#     Example:
#     ?- insert_at(alfa,[a,b,c,d],2,L).
#     L = [a,alfa,b,c,d]

list1 = ['a','b','c','d']
str1 = 'alfa'
k = 2
result1 = []

def insert_at_k(s1,l1,k1,r1):
	r1 = l1
	l1.insert(k1-1,s1)
	return r1

print insert_at_k(str1,list1,k,result1)