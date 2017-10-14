 # Create a list containing all integers within a given range.
 #    Example:
 #    ?- range(4,9,L).
 #    L = [4,5,6,7,8,9]

range1 = 4
range2 = 9
list1 = []

def list_int_range(r1,r2,l1):
	l1 = [i for i in range(r1,r2+1)]
	return l1

print list_int_range(range1,range2,list1)