import sys
sys.set_int_max_str_digits(100000)

for N in [4, 7, 20, 200, 2000]:
    result = 1
    i = 1
    while i <= N:
        a = result
        b = i
        while b > 0:
            a, b = b, a % b
        result = result * i // a
        i = i + 1
    print("1 ~", N, "->", result)