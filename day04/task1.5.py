number = int(input("Enter a number: "))
result = ""

# Each condition is checked separately (if, not elif),
# so several letters can be printed. Example: 20 -> "bcd"
if number == 42:
    result = result + "a"
if number <= 21:
    result = result + "b"
if number % 2 == 0:
    result = result + "c"
if number / 2 < 21:
    result = result + "d"
if number % 2 == 1 and number >= 45:
    result = result + "e"

# No condition matched -> "f"
if result == "":
    result = "f"

print(result)
