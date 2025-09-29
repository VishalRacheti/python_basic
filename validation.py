#valid user input
#username is no more than 12 characters
#username must not conatin digits
#username must not contain any spaces


username = input("Enter the username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters.")

elif ' ' in username:
    print("Username must not contain spaces.")

elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")

else:
    print(f"Username is valid. {username}")  