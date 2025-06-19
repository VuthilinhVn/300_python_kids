import os
# sao chep noi dung cua mot file sang file khac
file_target = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data2.txt"
file_source = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

if os.path.exists(file_target):
    os.makedirs(file_target)

try:
    with open(file_source, 'r', encoding='utf-8') as source_file:
        content = source_file.read()

    with open(file_target, 'w', encoding='utf-8') as target_file:
        target_file.write(content)

except FileNotFoundError:
    print("k tim thay file")

except Exception as e:
    print(f"Loi {e}")