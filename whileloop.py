#here we will write a while loop

name=input("Please enter your name: ")

while name == "":
    print("Name cannot be empty. Please enter your name.")
    name=input("Please enter your name: ")
print("Hello, " + name + "!")
