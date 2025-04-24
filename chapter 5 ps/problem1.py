marks = {
    "Maths": 85,
    "English": 78,
    "Science": 92,
    "History": 88,
    "Geography": 90
}

mark = input("Enter subject name to get marks: ")
print(F"Marks in {mark} is {marks.get(mark)}.")