import string


def word_frequency(path="zen.txt"):
    try:
        with open(path) as file:
            words = file.read().lower().split()   # 대소문자 구분 없이 세려고 lower
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return {}
    frequency = {}
    for word in words:
        word = word.strip(string.punctuation)
        if word:
            frequency[word] = frequency.get(word, 0) + 1   # 처음 보면 0에서 시작해 +1
    for word, count in sorted(frequency.items(), key=lambda pair: -pair[1]):
        print(word, count)                 # 많이 나온 순서대로
    return frequency


word_frequency()
