l = [11,22,33,44]

# index = 0
# for i in l:
#     print(f"On {index}, {i} is present.")
#     index += 1

# this can be simple by enumerate function enumerate fun return index with item.

for index, i in enumerate(l):
    print(f"On {index}, {i} is present.")