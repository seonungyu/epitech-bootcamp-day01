celsius = [-10, 0, 17.6, 28, 100]
# map(함수, 리스트) = 리스트의 모든 값에 함수를 하나씩 적용. 화씨 = 섭씨 * 9 / 5 + 32
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print(fahrenheit)   # [14.0, 32.0, 63.68, 82.4, 212.0]
