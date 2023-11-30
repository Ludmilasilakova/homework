from functools import reduce
my_list = [11, 52, 85, 121, 2, 96, 1, 222]
max_value = reduce(max, my_list)
print(max_value)
