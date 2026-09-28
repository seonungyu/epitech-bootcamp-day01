# Count down from 10000 to 1 (step -1), keep only multiples of 7
for i in range(10000, 0, -1):
    if i % 7 == 0:
        print(i)
