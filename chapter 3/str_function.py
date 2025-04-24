name = "harry"

print(len(name)) # length of string
print(name.startswith("h")) # check if string starts with "h"
print(name.endswith("rry")) # check if string ends with "y"   
print(name.find("z")) # find the index of "a" in string, returns -1 if not found
print(name.capitalize()) # capitalize the first letter of string  Harry
print(name.upper()) # convert string to uppercase  HARRY
print(name.lower()) # convert string to lowercase  HARRY
print(name.replace("h", "H")) # replace "h" with "H" in string
print(name.count("r")) # count the number of occurrences of "r" in string 2
print(name.isalpha()) # check if string contains only alphabets
print(name.isdigit()) # check if string contains only digits
print(name.isalnum()) # check if string contains only alphanumeric characters
print(name.isnumeric()) # check if string contains only numeric characters
print(name.isdecimal()) # check if string contains only decimal characters
print(name.isidentifier()) # check if string is a valid identifier
print(name.title()) # convert string to title case
print(name.split()) # split string into list of words
print(name.join(["a", "b", "c"])) # join list of strings with name as separator
print(name.strip()) # remove leading and trailing whitespace from string
print(name.lstrip()) # remove leading whitespace from string
print(name.rstrip()) # remove trailing whitespace from string