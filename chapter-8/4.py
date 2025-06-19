file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        content.replace('.', '')
        content.replace(',', '')
        content.replace('“', '')
        content.replace("”", '')
        words = content.split()
        print(words)
        print(f"So luong tu trong van ban la: {len(words)}")
except FileNotFoundError:
    print("Khong tim thay file")

except Exception as e:
    print(f"Loi {e}")
