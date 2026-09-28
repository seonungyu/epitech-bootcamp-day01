numbers = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 666,
    "life": 42,
    "googol": 10 ** 100,  # in Python, 10^100 would be a XOR (= 110), not a power
    "jordan": 23,
    "life, the universe and everything": 42,
    "emergency": 911,
    "euler": 2.71828,
}
print(max(numbers, key=numbers.get))
