# Group the elements of a set into disjoint subsets.
# Note that we do not want permutations of the group members; 
# i.e. [[aldo,beat],...] is the same solution as [[beat,aldo],...].
# However, we make a difference between [[aldo,beat],[carla,david],...] and [[carla,david],[aldo,beat],...].

# You may find more about this combinatorial problem in a good book on 
# discrete mathematics under the term 'multinomial coefficients'.

#     a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons?
# 		 Write a predicate that generates all the possibilities via backtracking.
#     Example:
#     ?- group3([aldo,beat,carla,david,evi,flip,gary,hugo,ida],G1,G2,G3).
#     G1 = [aldo,beat], G2 = [carla,david,evi], G3 = [flip,gary,hugo,ida]
#     ...

import random

list1 = ['aldo','beat','carla','david','evi','flip','gary','hugo','ida']
group1,group2,group3 = [],[],[]

def set_into_disjoints1(l1,g1,g2,g3):
	g1,g2,g3 = [],[],[]
	g1_num,g2_num,g3_num = 2,3,4
	count1,count2,count3 = 0,0,0
	for x in range(len(l1)):
		n2 = random.sample(range(len(l1)),len(l1))
		if count1<g1_num:
			g1.append(l1[x])
			count1 += 1
		elif count2<g2_num:
			g2.append(l1[x])
			count2 += 1
		elif count3<4:
			g3.append(l1[x])
			count3 += 1  
	return g1,g2,g3

print set_into_disjoints1(list1, group1,group2,group3)

# 	b) Generalize the above predicate in a way that we can specify a list of group sizes
# 	   and the predicate will return a list of groups.

# 	Example:
# 	?- group([aldo,beat,carla,david,evi,flip,gary,hugo,ida],[2,2,5],Gs).
# 	Gs = [[aldo,beat],[carla,david],[evi,flip,gary,hugo,ida]]
# 	...

list2 = [2,5,2]
group = []

def set_into_disjoints2(l1,l2,g):
	g1,g2,g3,g = [],[],[],[]
	count1,count2,count3 = 0,0,0
	g1_num,g2_num,g3_num = l2[0],l2[1],l2[2]
	for x in range(len(l1)):
		n2 = random.sample(range(len(l1)),len(l1))
		if count1<g1_num:
			g1.append(l1[x])
			count1 += 1
		elif count2<g2_num:
			g2.append(l1[x])
			count2 += 1
		elif count3<4:
			g3.append(l1[x])
			count3 += 1  
	g = [g1,g2,g3]
	return g

print set_into_disjoints2(list1,list2,group)