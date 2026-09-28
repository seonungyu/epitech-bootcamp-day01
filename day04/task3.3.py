# Vigenere cipher: like Caesar, but each letter uses a different shift
# taken from a key word. Key "abc" -> shifts 0, 1, 2, 0, 1, 2, ...


def vigenere(text, key, direction):
    # direction = 1 to encrypt, -1 to decrypt
    result = ""
    k = 0    # position in the key (only moves forward on letters)
    for letter in text:
        if letter.isalpha():
            key_shift = ord(key[k % len(key)].lower()) - ord("a")
            base = ord("a") if letter.islower() else ord("A")
            result = result + chr((ord(letter) - base + direction * key_shift) % 26 + base)
            k = k + 1
        else:
            result = result + letter
    return result


mode = input("Encrypt or decrypt? (e/d): ")
text = input("Enter the text: ")
key = input("Enter the key (letters only): ")

if mode == "e":
    print(vigenere(text, key, 1))
elif mode == "d":
    print(vigenere(text, key, -1))
else:
    print("Please type e or d")
