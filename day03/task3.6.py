import sys

# Average frequency (%) of each letter, accented letters included
languages = {
    "English": {"a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 12.7, "f": 2.2, "g": 2.0,
                "h": 6.1, "i": 7.0, "j": 0.15, "k": 0.77, "l": 4.0, "m": 2.4, "n": 6.7,
                "o": 7.5, "p": 1.9, "q": 0.1, "r": 6.0, "s": 6.3, "t": 9.1, "u": 2.8,
                "v": 1.0, "w": 2.4, "x": 0.15, "y": 2.0, "z": 0.07},
    "French":  {"a": 7.6, "b": 0.9, "c": 3.3, "d": 3.7, "e": 14.7, "f": 1.1, "g": 0.9,
                "h": 0.7, "i": 7.5, "j": 0.6, "k": 0.05, "l": 5.5, "m": 3.0, "n": 7.1,
                "o": 5.8, "p": 2.5, "q": 1.4, "r": 6.7, "s": 7.9, "t": 7.2, "u": 6.3,
                "v": 1.8, "w": 0.05, "x": 0.4, "y": 0.1, "z": 0.1,
                "é": 1.9, "è": 0.3, "ê": 0.2, "à": 0.5, "ç": 0.1, "ù": 0.05, "â": 0.05,
                "î": 0.05, "ô": 0.05, "û": 0.05},
    "Spanish": {"a": 11.5, "b": 2.2, "c": 4.0, "d": 5.0, "e": 12.2, "f": 0.7, "g": 1.8,
                "h": 0.7, "i": 6.2, "j": 0.5, "k": 0.01, "l": 5.0, "m": 3.2, "n": 6.7,
                "o": 8.7, "p": 2.5, "q": 0.9, "r": 6.9, "s": 8.0, "t": 4.6, "u": 2.9,
                "v": 1.1, "w": 0.02, "x": 0.2, "y": 1.0, "z": 0.5,
                "á": 0.5, "é": 0.4, "í": 0.7, "ó": 0.8, "ú": 0.2, "ñ": 0.3},
    "German":  {"a": 6.5, "b": 1.9, "c": 2.7, "d": 5.1, "e": 16.4, "f": 1.7, "g": 3.0,
                "h": 4.6, "i": 6.6, "j": 0.3, "k": 1.4, "l": 3.4, "m": 2.5, "n": 9.8,
                "o": 2.6, "p": 0.7, "q": 0.02, "r": 7.0, "s": 7.3, "t": 6.2, "u": 4.2,
                "v": 0.8, "w": 1.9, "x": 0.03, "y": 0.04, "z": 1.1,
                "ä": 0.6, "ö": 0.3, "ü": 0.7, "ß": 0.3},
}

# Read the text from a UTF-8 file (python task3.6.py file.txt), or from the keyboard
if len(sys.argv) > 1:
    f = open(sys.argv[1], encoding="utf-8")
    text = f.read().lower()
    f.close()
else:
    text = input("Type a text: ").lower()

# Count every letter, accented ones too (isalpha works with any alphabet)
counts = {}
total = 0
for c in text:
    if c.isalpha():
        counts[c] = counts.get(c, 0) + 1
        total = total + 1

for c in sorted(counts):
    print(c, counts[c])

# Compare with every letter known by us or by the language
best = ""
best_score = -1
for name in languages:
    freqs = languages[name]
    score = 0
    for c in set(counts) | set(freqs):
        mine = counts.get(c, 0) * 100 / total
        score = score + (mine - freqs.get(c, 0)) ** 2
    if best_score == -1 or score < best_score:
        best = name
        best_score = score

print("Language:", best)
