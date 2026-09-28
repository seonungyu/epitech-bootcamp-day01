def remove_duplicates(my_list):
    # A set cannot contain the same value twice
    return list(set(my_list))

print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 2]))
# 42, 42.0, 21+21 and 42*10/10 are all equal to 42: only 42 and '42' remain
print(remove_duplicates([42, '42', 42.0, 21 + 21, 42 * 10 / 10]))
