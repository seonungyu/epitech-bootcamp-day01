# filter(조건, 리스트) = 조건이 True인 것만 남김. 여기선 10보다 큰 것만
print(list(filter(lambda x: x > 10, [3.14, 101, 42, 666, -1])))   # [101, 42, 666]
