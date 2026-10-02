def letter_frequency(path="zen.txt"):
    try:
        with open(path) as file:
            text = file.read().lower()
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return {}
    frequency = {}
    for char in text:
        if char.isalpha():                 # 글자(a~z)만 세고 공백/문장부호는 건너뜀
            frequency[char] = frequency.get(char, 0) + 1
    for letter in sorted(frequency):       # 알파벳 순서대로
        print(letter, frequency[letter])
    return frequency


letter_frequency()
