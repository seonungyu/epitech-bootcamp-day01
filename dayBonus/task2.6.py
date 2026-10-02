def write():
    with open("toto.txt", "a") as file:   # "a" = append(덧붙이기): 기존 내용 뒤에 추가
        file.write("I'm a new line\n")


write()
