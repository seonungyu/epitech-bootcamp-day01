def my_sum(*args):                 # *args = 개수 상관없이 받은 값들을 튜플 하나로 묶음
    total = 0
    for value in args:
        if not isinstance(value, (int, float)):   # 숫자가 아니면
            raise ValueError(f"not a number: {value!r}")
        total += value
    print(total)
    return total


my_sum(1)                          # 1
my_sum(1, 2, 3)                    # 6
my_sum(-20, -10, 5, 5, 10, 10)     # 0
try:                               # 에러를 try로 잡아서 Traceback(빨간 에러 화면) 없이 메시지만
    my_sum(1, "toto")
except ValueError as error:
    print("ValueError:", error)
