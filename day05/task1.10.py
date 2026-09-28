# extend() adds every element of the second list at the end of the first one
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)

# * unpacks both lists inside a new list: same result, but a NEW list is created
my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)
