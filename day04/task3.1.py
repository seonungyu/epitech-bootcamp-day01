message = input("Enter a message: ")
key = int(input("Enter a key (1-25): "))

encrypted = ""
for letter in message:
    if letter.islower():
        # ord("a") = 97. Turn the letter into 0-25, shift, wrap with % 26, turn back
        encrypted = encrypted + chr((ord(letter) - ord("a") + key) % 26 + ord("a"))
    elif letter.isupper():
        encrypted = encrypted + chr((ord(letter) - ord("A") + key) % 26 + ord("A"))
    else:
        encrypted = encrypted + letter    # spaces, punctuation: unchanged
print(encrypted)
