dict_1 = {'name_1':'Vu Thi Linh'}


dict_2 = {'age': 27}

# su dung ** unpack
combine_dict = {**dict_1, **dict_2}

print(combine_dict)


# su dung update()

dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)