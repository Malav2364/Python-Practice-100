x = 4

#types of match cases

#simple match case  where we have to match 

# match x:
#     case 0:
#         print("X is zero")
#     case 1:
#         print("number is 1")
#     case 2:
#         print("number is 2")
#     case 3:
#         print("number is 3")
#     case 4:
#         print("number is 4")


#match case with if
name = str(input("Enter your name :"))
age = int(input("Enter your age :"))

match age:
    case _ if age < 18:
        print("It's some time for",name,"to drive a Car !!")
    case _ if age >= 18:
        print(name,"can Drive a Lambo !!")