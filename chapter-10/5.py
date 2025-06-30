def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not Found!"

    return content

print(read_file('./123.txt'))