first_names = ["Jackie", "Chuck", "Arnold", "Sylvester"]
last_names = ["Stallone", "Schwarzenegger", "Norris", "Chan"]
# last_names[::-1] = 거꾸로 뒤집기 → Chan, Norris, Schwarzenegger, Stallone
# zip = 두 리스트를 지퍼처럼 같은 자리끼리 짝지음 → (Jackie, Chan), (Chuck, Norris) ...
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])      # ('Jackie', 'Chan')
print(magic[1][0])   # Chuck   (두 번째 짝의 첫 번째)
print(magic[1][1])   # Norris  (두 번째 짝의 두 번째)
