#by slicing we will get the last 4 digits of the card number
card_number = "XXXX-XXXX-XXXX-5678"  #string
#card_number = input("Enter your credit card number: ")  #string
last_four_digits = card_number[-4:]  #slicing
print("The last four digits of your credit card are: " + last_four_digits)
