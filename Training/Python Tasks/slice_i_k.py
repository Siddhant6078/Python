# Extract a slice from a list.
#     Given two indices, I and K, the slice is the list containing the elements between the I'th and K'th element of the original list (both limits included). Start counting the elements with 1.

#     Example:
#     ?- slice([a,b,c,d,e,f,g,h,i,k],3,7,L).
#      L = [c,d,e,f,g]

list1 = ['a','b','c','d','e','f','g','h','i','k']
result1 = []
def slice_i_k(l1,n1,n2,r1):
	r1 = []
	return l1[(n1-1):n2]

print slice_i_k(list1,3,7,result1)