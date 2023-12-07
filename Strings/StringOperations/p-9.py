a = "Malav!!!! Patel Malav"
print(len(a)) #to get the length of string
print(a.upper()) #to upper case a string
print(a.lower()) #to lower case a string

#string are immutable or they are not changed 

print(a.rstrip("!")) #to trim the character passed in the parmeter
print(a.replace("Malav!!!!", "Hello"))#to replace the string with any other string 
print(a.split(" "))# splits the characters having the space and place them into the list 

name = "malav"
print(name.capitalize()) #used to capitalize the initial of a word in a string

head = "Welcome Back"
print(head.center(20)) #we have to pass no. of spaces to get spaces and align it
print(len(head.center(20)))#we will get length as per the spaces 

print(a.count("a")) #to count given characters in the string 
print(head.endswith("Back"))#to check the ending of a string 

heading = "Welcome Back Guys!!"
print(heading.endswith("Back", 4, 12)) #here we are giving it start  and end character tto check in

print(heading.find("Guys"))# here we can find any character from the strting by giving the finding character

print(heading.index("Welcome")) #to find index of characters in the string 

str1 = "Malav              "
print(str1.isalnum())#to check weather it is alphanumeric or not 
print(str1.isalpha())#to check weatheri it is alphebetic or not 
print(str1.isnumeric())#to check weather it is numeric or not 
print(str1.isupper())#to check weather it is uppercase or not or not 
print(str1.isspace())#to check weather it contains white spaces or tab spces

test1 = "Malav Patel"
print(test1.istitle()) #if first letter is capital then its a title 

print(test1.swapcase()) #swap upper to lower and lower to upper

title = "this is a title and is being used in our website"
print(title.title()) #converts text in title 