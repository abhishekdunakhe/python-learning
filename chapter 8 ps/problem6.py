
def rem_word(l, word):
    new_list = []
    for item in l:
        if not (item == word):
            new_list.append(item.strip(word))
    return new_list


l = ["Abhi", "Rohan", "Shubham", "anan"]

print(rem_word(l, "an"))