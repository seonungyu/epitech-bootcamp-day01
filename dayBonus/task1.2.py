animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]
# key = "무엇을 기준으로 줄 세울지" 알려주는 함수. 각 [이름, 숫자]에서 [1](숫자)을 기준으로!
sortedCounts = sorted(animalsCounts, key=lambda pair: pair[1])
print(sortedCounts)   # [['dog', 3], ['elephant', 42], ['cat', 666]]
