# This code will tell you how long to cook your turkey based on its weight in pounds.

## Enter turkey weight here.
answer="yes"
turkeys= float(input("How many turkeys do you have? "))

while answer=="yes":
    pounds= float(input("How many pounds is your turkey? "))
    cook_time= pounds * 13
    print("Cook your turkey for " + str(cook_time) + " minutes at 350 degrees.")
    answer = input("Enter yes or no to continue: ")
    continue


for i in range(2):
    sides = input("What sides are you going to have with your turkey? ")
    print("You will have "  + sides + " with your turkey.")
    for j in range(2):
        drinks = input("What are you going to drink with your meal? ")
        print("You will drink " + drinks + " with your meal.")
        break

 ## 13 minutes per pound at 350°F for an unstuffed turkey

