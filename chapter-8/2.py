
file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data1.txt"

noidung = "toi la vu thi linh!"
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(noidung)
except FileNotFoundError:
    print("Khong tim thay file!")

except Exception as e:
    print(f"Loi {e}")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Noi dung file da thay doi la: ")
        print(content)
except FileNotFoundError:
    print("Khong tim thay file")

except Exception as e:
    print(f"Loi {e}")