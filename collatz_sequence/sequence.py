#Created by: Patricia Sunday
#Date: September 11, 2025
def collatz(number):
    """Performs one iteration of the collatz sequence. If number is even, it's divided in half.
    If number is odd, it's multiplied by three and one is added

    :param number: The current value of the sequence
    :type number: int
    :return: The next value in the sequence
    :rtype: int
    """
    if number % 2 == 0:
        next_number = number // 2
    else:
        next_number = 3 * number + 1

    print(next_number, end=' ') 
    return next_number

while True:
    try:
        integer = int(input('Enter a number:\n'))
        print(integer, end=' ')

        #run collatz sequence until 1 is reached
        while integer != 1:
            integer = collatz(integer)
        break
    except ValueError:
        print('Please enter an integer.\n')