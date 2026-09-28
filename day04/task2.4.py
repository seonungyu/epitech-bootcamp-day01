for i in range(-30, 31):
    # Check "3 and 5" FIRST, otherwise 15 would stop at "Fizz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
