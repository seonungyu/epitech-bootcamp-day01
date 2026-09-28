LETTER_SCORES = {
    "AEIOULNSTR": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}

def scrabble_score(word):
    score = 0
    for letter in word.upper():
        for letters, points in LETTER_SCORES.items():
            if letter in letters:
                score += points
    return score

print(scrabble_score("python"))
print(scrabble_score("Epitech"))
