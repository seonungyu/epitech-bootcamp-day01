def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

def sandwich(veg=False):
    bread()
    if veg:
        lettuce()
        lettuce()
        tomato()
        tomato()
    else:
        lettuce()
        tomato()
        ham()
        ham()
    bread()

def make_sandwiches(n, veg=False):
    if isinstance(n, int) and n > 0:
        for i in range(n):
            sandwich(veg)
            print()
    else:
        print("I can't do this!")

make_sandwiches(1)
make_sandwiches(1, veg=True)
make_sandwiches(3.14)