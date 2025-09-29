#principle amount calculation

principle= 0
rate= 0
time= 0

while principle <= 0:
    principle = float(input("Enter the principle amount (greater than 0): "))
    if principle <= 0:
        print("Principle amount must be greater than 0.")
    
while rate <= 0:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate of interest must be greater than 0.")

while time <= 0:
    time = float(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0.")   

amount = principle * (1 + (rate / 100) * time)
print(f"The total amount after {time} years is: {amount}")
