import string


def longest(path="zen.txt"):
    try:
        with open(path) as file:
            words = file.read().split()    # 공백/줄바꿈 기준으로 단어 자르기
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return
    words = [w.strip(string.punctuation) for w in words]   # 앞뒤 . , ! - 같은 문장부호 떼기
    if not words:
        print(f"Error: {path} is empty")
        return
    print(max(words, key=len))             # 길이(len)가 가장 큰 단어


longest()
