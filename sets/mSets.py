from turtle import clear


setm = {"Malav", "Patel", 1,2,3, (1,2,3)}

#adding elements in sets and it will add the element at the last index of the set
setm.add("2364")
setm.add("OP")

#if added any element to original set than it will also add the same to the copied set
#to copy the set into another variable
# setA = setm.copy()
# print("copied",setA)

#it will clear the original set but the copied version will be as it was
# setm.clear()

set2 = {2,3,6,4}
set3 = {4,5,2,3}

#UNION of sets means it will group all elements from both the sets but repeated ones will not be accepted
print(set2.union(set3))

cities = {"Tokyo", "Berlin", "Madrid", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Madrid", "Kabul"}

cities3 = cities.union(cities2) 

#merged the sets and updated the cities set
cities.update(cities2)
# print(cities)

#intersection
# print(cities.intersection(cities2)) 
a = cities.intersection_update(cities2)
# print(a)

cities4 = cities.difference(cities2)
# print(cities4)


stm1 = {2,3,6,4}
stm2 = {2,2,7,4}

#difference of the set
dstm = stm1.difference(stm2)
# print(dstm)

#update methods
#add
stm1.add(1)
#remove
stm1.discard(10) #no error raised if we try to remove non existance element

stm1.remove(1) #it will raise error if non existance element found

#pop random item
item = stm1.pop()

#delete set
# del stm1

#clear methods to clean elements in the set

stm1.clear()
# print(stm1)


#disjoint sets means no thing in common
# print(stm1.isdisjoint(stm2))
#contains same elements 
# print(stm1.issubset(stm2))
#if all elements are present in either of the sets 
# print(stm1.issuperset(stm2))

#conditions in sets

sname1 = {"Malav","Patel", 2364}

if "Malav" in sname1:
    print("Verified")
else:
    print("Not-Verified")