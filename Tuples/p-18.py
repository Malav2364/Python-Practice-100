#tuples
# tup1 = (1,2,3,4)
# print(type(tup1))
# print(tup1[0])
# print(tup1[1])  #indexing in tuple 
# print(tup1[2])
# print(tup1.index(2)) #for finding the index in tuple 
# print(tup1.count(1))
#to manipulate tuple we need to perform the following steps
tuple1 = (0,1,1,2,2,3,3,4,2,1,6)
l1 = list(tuple1) #conversoin of tuple into list
# print(l1)
l1.append(5)
l1.pop(0)
tuple1 = tuple(l1)
# print(tuple1)

tpl1 = (0,1,2,3,2,3,1,3,2,3)
# res = tpl1.count(1)
res = tpl1.index(3,4,8)
print(res)

