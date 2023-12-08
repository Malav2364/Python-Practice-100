# a = int(input("Enter your age :"))
# print("Your age is :", a)

# print(a>18)
# print(a<18)
# print(a==18)
# print(a>=18)            #conditional operators
# print(a<=18)
# print(a!=18)

# if (a>=18):         #colon is important
#     print("You can have a sim card")
# else:                                                                    #simple if-else
#     print("First grow then come little kid !!")        #indentaion is important 

# appleprice = 210
# budget = 200

# if (appleprice <=budget):
#     print("Alexa add 1kg apples in the cart")
# else:
#     print("Alexa Don't add Apples to the cart")


#elif condition
appleprice = 10
budget = 200

if (budget - appleprice > 50):
    print("Add to Cart")
elif(budget - appleprice > 70):
    print("Its okay you can buy")
else:
    print("Don't add")

