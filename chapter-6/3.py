# su dung remove()
my_set = set([1, 2, 3, 4, 5])
my_set.remove(1)
#my_set.remove('banana') # se bi error
print(my_set)

# su dung discard()
my_set1 = set([1, 2, 3, 4, 5])
my_set1.discard(3)
my_set1.discard('banana') # <- k co error
print(my_set1)