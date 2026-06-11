try:
    file = open("sample.txt","r")
    print("reading file content")
    for line in file:
        print(line)
    file.close()

except FileNotFoundError:
    print("sample.txt does not exist")

