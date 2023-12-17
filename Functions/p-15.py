
def addProd(a,b,c,d):
    ap = ((a+b) + (c*d))
    print(ap)


def voteCriteria(age):
    if (age >= 18):
        print("You can Vote Now !!")
    else:
        print("Oho! You can't Vote !! caue you are just", age)

# voteCriteria(18)

#table printing function

def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

# table(79)

#practice of Functions

# def function name (arg){
#     code here
# }

def fname(dob):
    if dob == 2004:
        print("OK")
    else:
        print("Not OK")

fname(2004)

