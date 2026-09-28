# Decrypt a Caesar cipher WITHOUT knowing the key:
# try all 25 keys, and pick the one that looks most like English.

# How often each letter appears in normal English text (in %)
ENGLISH = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
           6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]


def shift(text, key):
    result = ""
    for letter in text:
        if letter.islower():
            result = result + chr((ord(letter) - ord("a") + key) % 26 + ord("a"))
        elif letter.isupper():
            result = result + chr((ord(letter) - ord("A") + key) % 26 + ord("A"))
        else:
            result = result + letter
    return result


def english_score(text):
    # Higher score = letters are distributed more like English
    score = 0
    for letter in text.lower():
        if "a" <= letter <= "z":
            score = score + ENGLISH[ord(letter) - ord("a")]
    return score


cipher = input("Enter the encrypted message: ")

best_key = 1
best_score = -1
for key in range(1, 26):
    candidate = shift(cipher, -key)
    print(key, ":", candidate)
    if english_score(candidate) > best_score:
        best_score = english_score(candidate)
        best_key = key

print()
print("Most likely key:", best_key)
print("Decrypted message:", shift(cipher, -best_key))
