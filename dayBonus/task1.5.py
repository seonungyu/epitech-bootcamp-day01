def check_even(n):
    return n % 2 == 0          # 2로 나눈 나머지가 0이면 짝수 → True


print(list(filter(check_even, [1, 2, 3, 4, 5, 6])))   # [2, 4, 6]
