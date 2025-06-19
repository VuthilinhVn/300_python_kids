file_path = "C:/Users/vulin/Desktop/300_python_kids/chapter-8/data .txt"

try:
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        content.replace(',', '')
        content.replace('.', '')
        content.replace(' ', '')
        content.replace('“', '')
        content.replace('”', '')
        content.replace('’', '')
        filter_content = ''.join(c for c in content if c not in ('','\n','\t'))
        char_count = len(filter_content)
        print(char_count)
        print(filter_content)
except FileNotFoundError:
    print("Khong tim thay file!")

except Exception as e:
    print(f"Loi {e}")