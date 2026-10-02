def my_division(a, b):
    try:
        return a // b, a % b       # // = 몫, % = 나머지. 쉼표로 두 개를 한 번에 돌려줌
    except ZeroDivisionError:
        print("Error: division by zero")
    except TypeError:
        print("Error: both parameters must be integers")


result = my_division(42, 4)
if result:
    quotient, remainder = result   # 돌려받은 두 값을 각각 변수에 나눠 담기
    print(quotient)                # 10
    print(remainder)               # 2
my_division(42, 0)
my_division(42, "toto")
