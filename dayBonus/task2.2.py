def read_line(path="zen.txt"):
    try:
        with open(path) as file:
            empty = True
            for line in file:          # 파일을 for로 돌리면 한 줄씩 나옴
                empty = False
                print(line, end="")    # 줄 끝에 이미 \n이 있어서 end=""
            if empty:
                print(f"Error: {path} is empty")
    except FileNotFoundError:
        print(f"Error: {path} does not exist")
    except PermissionError:
        print(f"Error: {path} is not readable")


read_line()
