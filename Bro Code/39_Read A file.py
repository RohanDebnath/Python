with open("C:\\Users\\USER\\Desktop\\textfile.txt") as file:
    print(file.read())

try:
    with open("C:\\Users\\USER\\Desktop\\textfile.tt") as file:
         print(file.read())
except FileNotFoundError:
    print("File not found")