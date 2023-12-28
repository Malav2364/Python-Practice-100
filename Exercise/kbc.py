questions = [
        ["What is your name ?", "malav", "aarav", "suraj", "chanda", 1],
        ["What is your name ?", "malav", "aarav", "suraj", "chanda", 1],
        ["What is your name ?", "malav", "aarav", "suraj", "chanda", 1],
        ["What is your name ?", "malav", "aarav", "suraj", "chanda", 1]
    ]

levels = [1000,2000,4000,8000,10000,50000,100000]

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}           b.{question[2]}")
    print(f"a. {question[3]}           b.{question[4]}")
    reply = int(input("Enter your answer (1-4) :"))
    if (reply == question[-1]):
        print(f"Correct answer you won Rs. {levels[i]}")
    else:
        print("Wrong Answer!")
