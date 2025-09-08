#1)
import random
dice = int(input("How many dice do you want to roll? "))

total = 0

for i in range(dice):
    roll = random.randint(1, 6)  # Random number between 1 and 6
    print(f"Dice {i+1}: {roll}")
    total += roll

print(f"The total sum of the dice is: {total}")

#2)
list = []
while True:
    user = input("Enter a number: ")
    if user == "":
        break
    list.append(int(user))

list.sort(reverse=True)
top_five = list[:5]

print("The five greatest numbers in descending order are:", top_five)

#3)
num = int(input("Enter an integer: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

#5)
list = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    list.append(city)

print("\nThe cities you entered are:")
for city in list:
    print(city)