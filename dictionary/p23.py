#this is about dictionaries in python

#creation of a dictionary in python 
#dict name and then in {} write data 
#example 

malav = {
    "Malav" : "Human-being",
    "Spoon" : "Object"
}

#accessing the 
# print(malav["Malav"])

emp = {
    2 : "Malav",
    1 : "Aarav",
    4 : "Saurav",
    5 : "Nirav",
    3 : "Jirav",
}

#accessing particluar key value pairs from the dictionary 

# print(emp) #for full access
# print(emp[4]) #for particular value access from the key (will get error)
# print(emp.get(10)) #for not getting error if the key doesn't exist 

# print(emp.keys()) #to get all keys of the dictionary

# for key in emp.keys():
#     print(f"key {key} -> value {emp[key]}")       #for all keys of the dictionaries

print(emp.items()) #returns the items in ley value pairs

for key, value in emp.items():  #prints the key and value both 
    print(key, value)
