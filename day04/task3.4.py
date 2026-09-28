# Break a Vigenere cipher when we know the key LENGTH but not the key.
# Idea: with key length 3, letters 1, 4, 7, ... all use the same shift,
# so each of those groups is just a Caesar cipher -> solve each one
# like task3.2 (pick the shift that looks most like English).

ENGLISH = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
           6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]


def best_shift(letters):
    # Try all 26 shifts; the best one makes the group look most like English.
    # Chi-squared: sum of (seen - expected)^2 / expected. Smaller = closer to English.
    best = 0
    best_error = None
    for s in range(26):
        counts = [0] * 26
        for letter in letters:
            counts[(ord(letter) - ord("a") - s) % 26] += 1
        error = 0
        for i in range(26):
            expected = ENGLISH[i] / 100 * len(letters)
            error = error + (counts[i] - expected) ** 2 / expected
        if best_error is None or error < best_error:
            best_error = error
            best = s
    return best


def vigenere(text, key, direction):
    result = ""
    k = 0
    for letter in text:
        if letter.isalpha():
            key_shift = ord(key[k % len(key)]) - ord("a")
            base = ord("a") if letter.islower() else ord("A")
            result = result + chr((ord(letter) - base + direction * key_shift) % 26 + base)
            k = k + 1
        else:
            result = result + letter
    return result


cipher = input("Enter the encrypted text: ")
length = int(input("Enter the key length: "))

letters = [c.lower() for c in cipher if c.isalpha()]
key = ""
for i in range(length):
    group = letters[i::length]          # every length-th letter, starting at i
    key = key + chr(best_shift(group) + ord("a"))

print("Key found:", key)
print("Decrypted text:", vigenere(cipher, key, -1))
