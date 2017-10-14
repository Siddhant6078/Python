# Sorting a list of lists according to length of sublists
#     a) We suppose that a list (InList) contains elements that are lists themselves. The objective is to sort the elements of InList according to their length. E.g. short lists first, longer lists later, or vice versa.

#     Example:
#     ?- lsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
#     L = [[o], [d, e], [d, e], [m, n], [a, b, c], [f, g, h], [i, j, k, l]]

list1 = [['a','b','c'],['d','e'],['f','g','h'],['d','e'],['i','j','k','l'],['m','n'],['o']]
result1 = []

def sort_as_sublist1(l1,r1):
	r1 = []
	r1 = sorted(l1, key=len)
	return r1

print sort_as_sublist1(list1,result1)


#     b) Again, we suppose that a list (InList) contains elements that are lists themselves.
# 		 But this time the objective is to sort the elements of InList according to their length frequency;
#		 i.e. in the default, where sorting is done ascendingly, lists with rare lengths are placed first,
#		 others with a more frequent length come later.

#     Example:
#     ?- lfsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
#     L = [[i, j, k, l], [o], [a, b, c], [f, g, h], [d, e], [d, e], [m, n]]

#     Note that in the above example, the first two lists in the result L have length 4 and 1,
#	  both lengths appear just once. The third and forth list have length 3;
#	  there are two list of this length. And finally, the last three lists have length 2.
#	  This is the most frequent length.

# def sort_as_sublist2(l2,r2):
# 	r2,r3 = [],[]
# 	dict1 ={}
# 	for x in l2:
# 		r2.append(len(x))
# 		r3.append(r2.count(len(x)))
# 		dict1 = dict1{r2:r3}
# 	return dict1

# print sort_as_sublist2(list1,result1)

dict2 = {1:'Sid'}
print dict2[1]