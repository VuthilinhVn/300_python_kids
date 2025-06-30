try:
    my_lst = [1, 2, 3]
    value = my_lst[5]

except IndexError:
    value = "Error: Index out of range!"

print(value)