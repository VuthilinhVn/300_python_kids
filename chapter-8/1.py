import os

file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'r',encoding='utf-8') as file: # python se mo file va tu dong dong sau khi doan ma trong with ket thuc
        content = file.read()
        print("noi dung cua file: ")
        print(content)

except FileNotFoundError:
    print("Khong tim thay file")

except Exception as e:
    print(f"Da xay ra loi {e}")