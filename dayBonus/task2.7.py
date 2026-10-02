def rewrite():
    try:
        with open("zen.txt") as source:
            content = source.read()
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return
    with open("toto.txt", "w") as target:   # "w" = 기존 내용을 지우고 새로 쓰기
        target.write(content)


rewrite()
