#breaks statement

# for i in range(12):
#     if (i == 1):
#         break               #here we have given a break in the for loop after the table passes 10 value
#     print("5 X",i+1,"=",5*(i+1))


# for m in range(12):
#     if (m>5):
#         print("Skipped")
#         continue                   #here the continue statement is used to skip the iteration
#     print("5 X",m+1,"=",5*(m+1))

#print odd even using continue statement 
# from os import name


# for i in range(1,100):
#     if (i%2 == 0):
#         print("Even :", i)
#         continue
#     print("Odd :",i)

#example of Break statement

#emulate do while loop using break
from ast import While


limit = int(input("Enter Limit of Numbers :"))
num = int(input("Enter number :"))

while True:
    print("Checking !")
    if (num > limit):
        print("Loop exited")
        break
    elif(limit > num):
        print("In Line !")
        break

    

    