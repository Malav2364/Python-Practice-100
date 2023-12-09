#python program to print table in python
num = 2
for i in range(1, 11):
    print(num,'*',i,'=',num*i)

#python program to print square of numbers
for i in range(1,6):
    print("Square of",i,"is",i*i)

#python program to find factorial of a number

number = int(input("Enter a number :"))
fact = 1
for i in range(1, number+1):
    fact*=i
print(fact)
