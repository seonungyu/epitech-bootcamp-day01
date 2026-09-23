text = input("Type a string: ")
result = ""
for word in text.split():
    result = result + word[0]
print(result)
