#typecasting in python

a = "1" #string
b = "2" #string
# print(a + b) #the output will be lol "12"

#to fix it we need to use type casting for the same 
#explicit means to explicitly convert the data type 
print(int(a) + int(b))

#impliit type casting means that the conversion takes place automatically by the python

c = 1.3  #float
d = 8    #integer
print(c + d) #result will be converted into float
