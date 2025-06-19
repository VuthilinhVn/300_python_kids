
file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n Toi la vu thi linh!")
        print("Noi dung da duoc them vao cuoi file")
except FileNotFoundError:
    print("Khong tim thay file")
except Exception as e:
    print(f"Loi {e}")