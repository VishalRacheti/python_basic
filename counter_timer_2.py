#This is counter timer

import time

countdown= int(input("Enter the countdown time in seconds: "))

for i in range(0, countdown):
    print(i)
    time.sleep(1)  # Pause for 1 second
print("Time is up!")