#Created by: Patricia Sunday
#Date: September 10, 2025
import random
import sys

print('Welcome to Integer Whisperer! - your one stop shop for basic integer insights')

mainLoop = True
while mainLoop:
    number = int(input('Enter an integer: '))
    print()

    #randomize comment
    numDesc = 'Your number is '
    if random.randint(0,10)  > 5:
        numDesc += 'an interesting choice!'
    else:
        numDesc += 'a solid choice!'

    #check prime number
    prime = True
    if number < 0: #for negative numbers
        prime = False
    else: #if positive number
        for i in range(2,number):
            if number%i == 0:
                prime = False

    print(numDesc)
    print('The whisperer says ' + str(number) + ' is...')

    #print prime insights
    if number == 0 or number == 1:
        print("- Neither prime nor composite! There's no fun insights")
    elif prime == True:
        print('- A prime number!')
    else: #if composite, show factor(s) -- with 10 as max factor
        for i in range(2,11):
            if number%i == 0:
                print('- Divisible by ' + str(i) + '!')
            
            #break out of loop once final possible factor is reached to save iterations
            if i == number-1:
                break

    #prompt to continue
    while True:
        loopChoice = str(input('\nWould you like to enter another integer? Enter Yes or No: ')).lower()
        if loopChoice == 'no':
            mainLoop = False
            break
        elif loopChoice == 'yes':
            break