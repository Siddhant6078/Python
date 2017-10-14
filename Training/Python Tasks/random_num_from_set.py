 # Lotto: Draw N different random numbers from the set 1..M.
 #    The selected numbers shall be put into a result list.
 #    Example:
 #    ?- lotto(6,49,L).
 #    L = [23,1,17,33,21,37]

 #    Hint: Combine the solutions of problems 1.22 and 1.23.
import random
list1 = []
num1 = 6
num2 = 49

def lotto(n1,n2,l1):
 	l1 = []
 	n3 = ''
	for x in range(n1):
		n3 = random.randrange(1,n2)
		l1.append(n3)
	return l1

print lotto(num1,num2,list1)