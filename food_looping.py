#here we will loop the food input until user enters 'exit'

food= input("Enter the food you like (type 'q' to quit): ")

while not food == 'q':
    print("You like " + food)
    food= input("Enter the food you like (type 'q' to quit): ")