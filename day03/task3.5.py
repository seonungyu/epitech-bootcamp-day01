# Average frequency (%) of each letter a..z in each language
letters = "abcdefghijklmnopqrstuvwxyz"
languages = {
    "English": [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
                6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.15, 2.0, 0.07],
    "French":  [7.6, 0.9, 3.3, 3.7, 14.7, 1.1, 0.9, 0.7, 7.5, 0.6, 0.05, 5.5, 3.0,
                7.1, 5.8, 2.5, 1.4, 6.7, 7.9, 7.2, 6.3, 1.8, 0.05, 0.4, 0.1, 0.1],
    "Spanish": [11.5, 2.2, 4.0, 5.0, 12.2, 0.7, 1.8, 0.7, 6.2, 0.5, 0.01, 5.0, 3.2,
                6.7, 8.7, 2.5, 0.9, 6.9, 8.0, 4.6, 2.9, 1.1, 0.02, 0.2, 1.0, 0.5],
    "German":  [6.5, 1.9, 2.7, 5.1, 16.4, 1.7, 3.0, 4.6, 6.6, 0.3, 1.4, 3.4, 2.5,
                9.8, 2.6, 0.7, 0.02, 7.0, 7.3, 6.2, 4.2, 0.8, 1.9, 0.03, 0.04, 1.1],
}

text = input("Type a text: ").lower()

# Count each letter
counts = {}
total = 0
for c in text:
    if c in letters:
        counts[c] = counts.get(c, 0) + 1
        total = total + 1

for c in sorted(counts):
    print(c, counts[c])

# The language whose frequencies are closest to ours wins
best = ""
best_score = -1
for name in languages:
    score = 0
    for i in range(len(letters)):
        mine = counts.get(letters[i], 0) * 100 / total
        score = score + (mine - languages[name][i]) ** 2
    if best_score == -1 or score < best_score:
        best = name
        best_score = score

print("Language:", best)
