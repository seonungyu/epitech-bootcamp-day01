# Original (broken) code:
#   a == 42          -> == compares, it does not store. Use =
#   b == 41
#   if a = b         -> = stores, it does not compare. Use ==, and add ':'
#   if b =< a        -> the operator is <=, not =<
#   if b =! a        -> the operator is !=, not =!
#   print(...)       -> the code inside an if must be indented
# Grammar also fixed in the messages.

a = 42
b = 41
if a == b:
    print("A and B are the same")
if b <= a:
    print("B is equal to or lower than A")
if b != a:
    print("B is different from A")
