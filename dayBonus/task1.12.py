def new_division(num, den, acc=1):
    try:
        print(f"{num / den:.{acc}f}")   # :.{acc}f = 소수점 아래 acc자리까지 반올림해서 표시
    except ZeroDivisionError:
        print("Error: division by zero")
    except (TypeError, ValueError):
        print("Error: num and den must be numbers, acc an integer")


new_division(8.4, 13)      # 0.6
new_division(8.4, 13, 6)   # 0.646154
new_division(1, 0)
