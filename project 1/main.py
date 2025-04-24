import random
'''
1 for snake
-1 for water
0 for gun
'''
computer_chose = random.choice([ -1, 0, 1 ])
you_chose = input("Enter your choise...")

game_dict = {"s" : 1, "w" :-1, "g" : 0}
game_rule = {1 : "snake", -1 : "water", 0 : "gun"}
convert_your_chose = game_dict[you_chose]

convert_my_to_game = game_rule[convert_your_chose]
convert_computer_to_game = game_rule[computer_chose]
print(f"you chose {convert_my_to_game} and computer mahashay chose {convert_computer_to_game}")

if(computer_chose == convert_your_chose):
    print("Game Draw..!")

else:
    '''
    if(computer_chose == -1 and convert_your_chose == 1):   -1 - 1 = 2
        print("You Win..!")

    elif(computer_chose == -1 and convert_your_chose == 0):     -1 - 0 = -1
        print("You lose..!")

    elif(computer_chose == 1 and convert_your_chose == -1):     1 - -1  = 2
        print("You lose..!")

    elif(computer_chose == 1 and convert_your_chose == 0):      1 - 0 = 1
        print("You Win..!")

    elif(computer_chose == 0 and convert_your_chose == -1):     0 - -1 = 1
        print("You Win..!")

    elif(computer_chose == 0 and convert_your_chose == 1):      0 - 1 = -1
        print("You lose..!")

    else:
        print("Something went wrong..!")
    '''
    if((computer_chose - convert_your_chose) == -1 or (computer_chose - convert_your_chose) == 2):
        print("You lose..!")
    else:
        print("You Win..!")
    

    