#recursion in python
#using same function within the function is called recursion in python
def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(1))

#fibonacci sequence print using python

def fc(n1):
    if(n1 == 0 | n1 == 1):
        return 1
    else:
        return n1 + fc(n1-1)
print(fc(10))
