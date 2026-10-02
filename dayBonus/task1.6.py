fruits = ['apple', 'banana', 'kiwi', 'pear']
# "4글자 넘는 걸 없애라" = "4글자 이하만 남겨라"
print(list(filter(lambda word: len(word) <= 4, fruits)))   # ['kiwi', 'pear']
