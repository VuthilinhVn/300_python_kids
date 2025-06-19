

file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
        print(f"So luong line trong file la: {line_count}")
except FileNotFoundError:
    print("Khong tim thay file!")

except Exception as e:
    print(f"Loi {e}")