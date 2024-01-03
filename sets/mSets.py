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
d = set2.union(set3)
print(d)

#in intersection 
e = set2.intersection(set3)
print(e)

# print(setm)