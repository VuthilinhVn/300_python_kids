import os
# kiem tra file ton tai chua:
file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"
folder_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/my_folder"

if os.path.isfile(file_path):
    print(f"{file_path} da ton tai")

else:
    print(f"{file_path} khong ton tai")


# kiem tra folder ton tai chua?
if os.path.exists(folder_path):
    print(f"{folder_path} da ton tai")

else:
    print(f"{folder_path} chua ton tai va da tao folder moi!")
    os.makedirs("C:/Users/vulin/Desktop/300_python_kids/chapter-8/my_folder")


# liet ke cac file / thu muc trong thu muc htai
file_name = os.listdir(".")
print(file_name)

# lay duong dan
print(os.getcwd())