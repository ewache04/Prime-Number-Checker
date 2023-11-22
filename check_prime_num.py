'''
Author: Jeremiah
Code Description: Check Prime Number
Last Updated Date: 3/27/2020
'''

import math


def get_number():
    try:
        n = int(input('Enter a number (or enter 0 to quit): '))
        result = n
    except ValueError:
        print('Please enter an integer.')
        result = None
    return result


def check_divisors(number):
    divisors_range = []
    try:
        for n in range(1, number + 1):
            divisors_range.append(n)
        result = divisors_range
    except ValueError:
        print('Please enter a number greater than 0.')
        result = None
    return result


def display_prime(number, divisors_list):
    pass_num = []
    fail_num = []

    for n in divisors_list:
        verifier = number % n
        if verifier == 0:
            pass_num.append(n)
        else:
            fail_num.append(n)

    pass_len = len(pass_num)

    if pass_len == 2:
        print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')


def main():
    while True:
        option = input('Do you want to check a number? (y/n): ').lower()

        if option != 'y':
            print('Exiting the program. Goodbye!')
            break

        number = get_number()

        if number is not None:
            if number == 0:
                print('Exiting the program. Goodbye!')
                break

            divisors_list = check_divisors(number)

            if divisors_list is not None:
                display_prime(number, divisors_list)


if __name__ == "__main__":
    main()
