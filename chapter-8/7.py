import os
file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/my_folder/1.py"

try:
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"file {file_path} da xoa")
    else:
        print(f"{file_path} khong ton tai")

except Exception as e:
    print(f"Loi {e}")