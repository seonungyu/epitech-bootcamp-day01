# For each x: if x is even, keep x // 2, otherwise x * 2
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
