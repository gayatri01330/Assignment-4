data = input("enter some text")
with open("output.txt","w") as file:
    file.write(data)
    more_data = input("Enter more text: ")

with open("output.txt", "a") as file:
    file.write("\n" + more_data)
print("Final file content:")

with open("output.txt", "r") as file:
    print(file.read())

