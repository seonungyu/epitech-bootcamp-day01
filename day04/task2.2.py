text = input("Enter a string: ")
result = ""
for letter in text:
    result = result + letter * 2    # "t" * 2 -> "tt"
print(result)
