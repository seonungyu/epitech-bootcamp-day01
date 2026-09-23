p = "abcdefghij"
step1 = p[::-2]       # backwards, one letter out of two -> "jhfdb"
step2 = step1[:5]     # first 5 letters (all of them)    -> "jhfdb"
step3 = step2[::-1]   # reversed                         -> "bdfhj"
step4 = step3[3:]     # drop the first 3 letters         -> "hj"
print(step1, step2, step3, step4)

# Simplified: start at index 7 ("h"), one letter out of two
print(p[7::2])
