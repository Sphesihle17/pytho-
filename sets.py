#Sets

my_set  = {1,2,3,4,5}
print(my_set)

my_set.add(6) #Add a new value
print(my_set)

my_set.remove(5) #Remove a new value
print(my_set)

#Using union
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

#Using intersection
inter_set  = set1.intersection(set2)
print(inter_set)

 #Using difference
dif_set  = set1.difference(set2)
print(dif_set)
