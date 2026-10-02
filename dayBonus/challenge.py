import sys

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def to_words(n):                   # 1 ~ 1000 을 영어 단어로 (띄어쓰기/하이픈 없이)
    if n == 1000:
        return "onethousand"
    words = ""
    if n >= 100:
        words += ONES[n // 100] + "hundred"   # 115 → "onehundred"
        n %= 100                              # 남은 15
        if n:
            words += "and"                    # 영국식: one hundred AND fifteen
    if n >= 20:
        words += TENS[n // 10] + ONES[n % 10] # 42 → "forty" + "two"
    else:
        words += ONES[n]                      # 0~19는 표에서 바로
    return words


def main():
    try:
        n = int(sys.argv[1])
        if not 1 <= n <= 1000:
            raise ValueError
    except (IndexError, ValueError):
        print("Usage: python challenge.py N   (1 <= N <= 1000)")
        return
    print(sum(len(to_words(i)) for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
