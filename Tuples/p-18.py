#tuples
tup1 = (1,2,3,4)
print(type(tup1))
print(tup1[0])
print(tup1[1])  #indexing in tuple 
print(tup1[2])
print(tup1.index(2)) #for finding the index in tuple 
print(tup1.count(1))

if 3 in tup1:
    print("It is in the tuple !!")


#for new tuple 
tup2 = tup1[1:3]
print(tup2)
#slicing in tuple 
