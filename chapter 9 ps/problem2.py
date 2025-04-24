import random

def game():
    print("Score Genereting...")
    score = random.randint(1,50)
    print(score)

    with open("chapter 9 ps/score.txt") as f:
        score_in_file = f.read()
        if(score_in_file != ""):
            score_in_file = int(score_in_file)
        else:
            score_in_file = 0

    if(score_in_file > score):
        with open("chapter 9 ps/score.txt", "w") as f:
            f.write(str(score))

    return score

game()
