from random import randint

n = randint(1,50)
a = -1
guessAttempt = 1

while(a != n):
    a = int(input("Enter Guess Number:::"))
    if(a>n):
        print("Enter Lower Number Please...")
        guessAttempt += 1

    elif(a < n):
        print("Enter Higher Number Please...")
        guessAttempt += 1


print(f"You guess The Number In {guessAttempt}.")






# fast api
# 