print("Let's play Kaun Banega Crorepati")

totalmoney=0
moneypercorrectanswer=5000

q1 = "What is the name of the first prophet in Islam?"
options = ["a) Adam(AS)", "b) Isa(AS)", "c) Ibrahim(AS)", "d) Muhammad(SAWS)"]
correct_answer = "a"

print(q1)
for option in options:
    print(option)

a1 = input("Your answer (a/b/c/d): ").lower()

if a1 == correct_answer:
    print("The answer is correct!")
    totalmoney+=moneypercorrectanswer
else:
    print("Sorry but the answer is wrong")

question2 = "Who was the last prophet?"
options = ["a) Adam(AS)", "b) Isa(AS)", "c) Ibrahim(AS)", "d) Muhammad(SAWS)"]
correct_answer = "d"

print(question2)
for option in options:
    print(option)

answer = input("Your answer (a/b/c/d): ").lower()

if answer == correct_answer:
    print("The answer is correct!")
    totalmoney+=moneypercorrectanswer
else:
    print("Sorry but the answer is wrong")

question = "Which prophet is referred to as God in christianity?"
options = ["a) Adam(AS)", "b) Isa(AS)", "c) Ibrahim(AS)", "d) Muhammad(SAWS)"]
correct_answer = "b"

print(question)
for option in options:
    print(option)

answer = input("Your answer (a/b/c/d): ").lower()

if answer == correct_answer:
    print("The answer is correct!")
    totalmoney+=moneypercorrectanswer
else:
    print("Sorry but the answer is wrong")


question = "For which Prophet was the fire cooled down by Allah?"
options = ["a) Adam(AS)", "b) Isa(AS)", "c) Ibrahim(AS)", "d) Muhammad(SAWS)"]
correct_answer = "c"

print(question)
for option in options:
    print(option)

answer = input("Your answer (a/b/c/d): ").lower()

if answer == correct_answer:
    print("The answer is correct!")
    totalmoney+=moneypercorrectanswer
else:
    print("Sorry but the answer is wrong")
print("You won: ", totalmoney,"rs")
