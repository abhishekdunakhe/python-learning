# C / 5 = (f-32)/9
# C = 5 * (f-32)/9

def c_to_f(f):
    return 5 * (f-32)/9

n = int(input("Enter Number...!"))
print(f"the value is in degree c {round(c_to_f(n),2)}C")