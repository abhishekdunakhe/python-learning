Marathi = int(input("Enter mark of Marathi:"))
Sanskrit = int(input("Enter mark of Sanskrit:"))
Hindi = int(input("Enter mark of Hindi:"))

total_percentage = ((Marathi + Sanskrit + Hindi) * 100) / 3

if(total_percentage >= 40 and Marathi >= 33 and Sanskrit >= 33 and Hindi >= 33):
    print("Yor are pass!")
else:
    print("You are fail!")
