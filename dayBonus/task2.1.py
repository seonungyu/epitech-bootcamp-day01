def read_file(path="primes.txt"):
    try:
        with open(path) as file:       # with = 다 쓰면 파일을 자동으로 닫아줌 (close 깜빡 방지)
            content = file.read()      # 파일 전체를 문자열 하나로 읽기
    except FileNotFoundError:
        print(f"Error: {path} does not exist")
        return
    except PermissionError:
        print(f"Error: {path} is not readable")
        return
    if not content:
        print(f"Error: {path} is empty")
        return
    print(content, end="")


read_file()
