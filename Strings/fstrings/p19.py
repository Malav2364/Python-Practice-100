#they are introduced in python version 3.6

letter = "My name is {1} and i am from {0}" #here we are taking value from other object 
country = "India" #define the object 
name = "Malav"  #define the object 


#use letter format to insert them into the main line.
# print(letter.format(country, name)) #we need to give them index for sequence


#f strings in python
print(f"My name is {name} and i am from {country}")    #use f string to get the value directly

price = 49.0999
print(f"The price is {price:.2f}")   #used to get only 2 number after the decimal points 

#calculations in String using f string 

calc = f"This is {2 * 30}"
print(type(calc)) #type is string
print(calc)
