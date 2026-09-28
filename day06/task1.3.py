def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

def make_sandwiches(n):
    if isinstance(n, int) and n > 0:
        for i in range(n):
            sandwich()
            print()
    else:
        print("I can't do this!")

make_sandwiches(2)
make_sandwiches(3.14)
make_sandwiches(-1)
