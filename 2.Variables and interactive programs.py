#1) Write a program that asks your name and then greets you by your name
name =input('Enter your name: ')
print("Hello, "+name+"!")


#2) Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius =float(input('Enter your radius: '))
area = 3.14*radius*radius
print("The are of the circle is: ", area)

#3)Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
length =float(input('Enter your length: '))
width =float(input('Enter your width: '))
perimeter = 2*(length+width)
area = length*width
print("The perimeter of the circle is: ", perimeter)
print("The area of the circle is: ", area)

#4) Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))
number3 = int(input('Enter your third number: '))
sum = number1+number2+number3
product = number1*number2*number3
average = (number1+number2+number3)/3
print("The sum of the three numbers is: ", sum)
print("The product of the three numbers is: ", product)
print("The average of the three numbers is: ", average)

#5) Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

talents = int(input('Enter your talents: '))
pounds = int(input('Enter your pounds: '))
lots = int(input('Enter your lots: '))
totalgram = (talents*20*32+pounds*32+lots)*13.3
kg = int(totalgram/1000)
g = totalgram % 1000
print("The weight in modern units: "+str(kg)+" kilograms and "+str(g)+" grams" )

#6)Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.

import random
code3 = [random.randint(0, 9) for _ in range(3)]
print("3-digit code: ", code3)
code4 = [random.randint(1, 6) for _ in range(4)]
print("4-digit code: ", code4)