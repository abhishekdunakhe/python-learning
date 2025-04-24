age = int(input("Enter Your Age: "))

if(age >= 18):
    print("You are eligible for voting!")

elif(age == 0):
    print("You are enter 0 which is not valid age!")

elif(age < 0):
    print("You are enter negative age which is not valid!")

else:
    print("You are not eligible for voting!")

print("End Of program!")
