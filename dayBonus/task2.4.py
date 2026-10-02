def count_lines(path):
    try:
        with open(path) as file:
            total = sum(1 for line in file)   # 한 줄 나올 때마다 1씩 더하기
    except (FileNotFoundError, PermissionError) as error:
        print("Error:", error)
        return
    print(f"{path}: {total} line(s)")


count_lines("zen.txt")
count_lines("primes.txt")
count_lines("nothing.txt")
