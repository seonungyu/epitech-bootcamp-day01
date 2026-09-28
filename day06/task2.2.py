def clean(text):
    result = ""
    for c in text:
        if c.isalnum():
            result = result + c.lower()
    return result

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ")
print(is_palindrome(clean(text)))
