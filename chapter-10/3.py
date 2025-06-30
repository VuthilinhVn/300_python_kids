try:
    my_dict = {"linh": 0, "vu": 1, "thi": 2}
    value = my_dict["cay"]

except KeyError:
    value = "Error: Key not found in dictionary!"


print(value)