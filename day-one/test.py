dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 1, 'y': 2, 'z': 1, 'w': 3, 'v': 1}

count_dict = {}

for value in dict1.values():
    count_dict[value] = list(dict2.values()).count(value)

print(count_dict)