#practice  of string funcitions and its operations

name = "Malav!!! Aarav Swapnil Gopi"

#length function to determine the length
print(len(name))

#upper and lower
print(name.upper())
print(name.lower())

#strip to give a parameter in it 
print(name.rstrip("!"))
#replace
print(name.replace("Malav", "Aarav"))

#split
print(name.split(" "))

#to capitalize  initial word
name1 = "malav"
print(name1.capitalize())

#to align string to center
head = "Welcome to my web Page"
print(head.center(50)) #according to spaces 
# print(len(head.center(50)))

#to count the specific chars in the string 
print(head.count("e"))

#to check the ending 
print(name1.endswith("alav"))
#to find an index value of 
print(name1.find("l"))

heading = "Welcome Back Guys !!"
#to get index of a word
print(heading.index("Back"))

str2 = "Malav Patel"
print(str2.isalnum())
print(str2.isalpha())
print(str2.isascii())
print(str2.islower())
print(str2.isupper())
print(str2.isspace())
print(str2.swapcase()) #used to swap form upper to lower and lower to upper

title1 = "Yo watsup guys i am the proest of the pro in the world !!"
print(title1.title()) #converts string  to title form
