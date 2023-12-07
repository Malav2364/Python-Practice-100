names = "Malav"
# print(names[0:6]) #print upto the no. of characters

len1 = len(names) #for calculating the length of the string
print("The length of My Name is :", len1)

#other variations of string printing 
print(names[:4]) #here if we dont give starting pointer than it will take 0 automatically
print(names[1:4])
print(names[3:4])
print(names[0:]) # in this case it will go to the max chars the word contains
print(names[0:-2])
print(names[-3:-1])

#loop through a string 
# for i in names:
#     print(i)

#question
name = "Harry"
print(name[-4:-2])
