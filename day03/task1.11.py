# print("hello" + 42) -> TypeError: can only concatenate str (not "int") to str
# A string and a number can't be added: convert the number to a string first.
print("hello" + str(42))
