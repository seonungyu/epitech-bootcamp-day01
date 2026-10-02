def ship(*names, **address):       # *names = 이름들(튜플), **address = 이름=값 쌍들(딕셔너리)
    print(" ".join(names))         # 이름들을 띄어쓰기로 이어붙이기
    for key, value in address.items():
        print(f"{key}: {value}")


ship("Batman", street="Mountain Drive", city="Gotham")
print()
ship("Superman", "The man of steel", apartment="3D", num=344,
     street="Clinton Street", city="Metropolis")
