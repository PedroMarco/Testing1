__author__ = 'acpb859'
import random

# Define 2 random numbers, sum them and present results. Do a boolean to see if true or false

number1 = random.randint(1,10)
number2 = random.randint(1,10)

if number1 < number2:
    number1, number2 = number2, number1

result = eval (input('What is '+str(number1) + '-' +str(number2) + '?'))

if result == (number1-number2):
    print('The answer is Right')
else:
    print('The answer is Wrong')
