l = [10,20,30,40]  #declaration of List
print(type(l))  #type check of list

#Calling of List or to access particular item in it like array 
#it can be changed 

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3]) 

l.append(10) #to add an item in the list Note appended will be treated as last item only until customized
# print(l.count(10)) #to count items in list
l.insert(1,4,) #to insert at a specific address first address and then items to be inserted
# l.clear() #to clear the list
cpylist = l.copy() #stores a copy of list
# cpylist.insert(1,7)
# l.insert(2,8)
# print("This is Copy of List -1 ",cpylist)

# print(l.index(8))
l.sort() #once sorted it will print sorted one in the main print statement

l.reverse() #vice versa as above
l.pop(0) #to delete an element in the list using the index of the element

# print(l)

if  30 in l:
    print("Available !!")
else:                  #to check elements present in the list or not 
    print("Nahi Hai!!")

print(l[1:]) #print list from index 1 till last index
print(l[1:4:3]) #jump index here the last number indicates the index we have to jump

