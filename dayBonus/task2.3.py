def read_lines(*numbers, path="primes.txt"):
    try:
        with open(path) as file:
            lines = file.readlines()   # 모든 줄을 리스트로: lines[0]이 1번째 줄
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return
    for n in numbers:
        if not isinstance(n, int) or not 1 <= n <= len(lines):
            print(f"Error: line {n} does not exist (1-{len(lines)})")
        else:
            print(lines[n - 1], end="")   # 사람은 1부터, 리스트는 0부터 세서 -1


read_lines(666)          # 666 4973
read_lines(1, 2, 3)
read_lines(20000)        # 에러
