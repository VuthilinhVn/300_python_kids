
file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("k tim thay file")

except Exception as e:
    print(f"Loi {e}")