num = [1,2,3,4,5,6,7,8,9,0]

even = list(filter(lambda x : x%2 == 0, num))
print(even)  # [2, 4, 6, 8, 0]

names = ["CtAmerica","Hulk","IronMan",""]
non_empty = list(filter(lambda x: len(x) > 0, names))
print(non_empty)  # ['CtAmerica', 'Hulk', 'IronMan']