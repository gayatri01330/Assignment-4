try:
    with open("sample.txt", "r") as file:
    print("reading file content")
    for line in file:
        print(line)
    file.close()

except FileNotFoundError:
    print("sample.txt does not exist")

