def count_words(text):
    text = text.lower()
    total = 0
    for word in ["cat", "garden", "mice"]:
        total = total + text.count(word)
        total = total + text.count(word[::-1])
    return total

print(count_words("the CataCat attaCk a Cat"))
print(count_words("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))
