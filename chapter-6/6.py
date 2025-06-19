set_1 = set([1, 2, 3, 5, 6, 7])

set_2 = set([9, 1, 2, 10, 11, 12, 14, 16])

# hop cua 2 set co the dung | or union()

set_union1 = set_1 | set_2
print(set_union1)

set_11 = set_1.copy()

set_union2 = set_11.union(set_2)

print(set_11)
print(set_union2)

