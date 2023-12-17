def average(a = 25,b = 20):  #def args   #here in this case if we give arguments with value it will not consider if alredy called with the function
    print("The average is :", (a+b)/2)

# average(10,20) #it will get 1st priority
# average(10)#here the value of b will be derived from def  args. vice versa

def add(a,b=1): #here a is a REQUIRED argument and b has a default value
    print("Sum", a+b)

# add(10)

#variable length arguments

def avg(*numbers): #* means data stored in tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is :", sum / len(numbers)) #length of total numbers in a tuple

# avg(10,20,30,40)
    
ms = (10,20,30,40,50)  #it's a tuple 
# print(type(ms))

def name(**name):   #dictionary if there are * * it contains classs and objects
    print("Hello ,", name["fname"], name["mname"], name["lname"])

name(fname = "Malav", mname = "Swapnil", lname = 'Patel')