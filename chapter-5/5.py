my_dict = {'name':'Vu thi linh', 'age':27, 'major': 'Computer Science'}
key_find = input("Nhap tu khoa can tim kiem: ")

if key_find in my_dict.keys():
    print(f"{key_find} co trong dictionary")

else:
    print(f"{key_find} k co trong dictionary")