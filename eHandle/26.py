a = input("Enter the number :")
print(f"Multiplication table for the number {a}")

try:
    for i in range(1,11):
        print(int(a), "X", i, "=", int(a)*i)
# except Exception as e:
#     print(e)
# print(f"Chutto Chappal Khoti Jagya e Avse {a}!")
except ValueError :
    print("Sidho Reje hahaha")

#for handling errors we'll gona using try except to handle the errors