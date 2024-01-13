for i in range(5):
    print(i)
else: #at the end of the for loop else will be executed
    print("Baat Khatam !")

for i in range(10):
    print(i)
    if i==6:
        break  #here in this case ELSE will not execute because the loop is broken
else:
    print("Todi phodi ne navru!!")

#here the for loop should be compulasrily finished then and only then ELSE will be executetd

#same rules for while loop
ai = 0
while ai < 17:
    print(ai)
    ai = ai + 1
else:
    print("Else for While Loop")