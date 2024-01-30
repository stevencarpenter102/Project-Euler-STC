from math import *


def problem_3a(number):
    """
    Find the largest prime number (slow way)
    Works for numbers larger than 5
    """
    largest_prime = 0
    temp_num = int(number / 2)

    for x in range(temp_num, 2, -1):
        if number % x == 0:
            largest_prime = problem_3a(x)  # reached a possible prime number
            break
        if x == 3:
            largest_prime = number
    if(temp_num < 4):
        largest_prime = number

    return largest_prime


def problem_3b(number):
    """
    Find the largest prime number (fast way)
    Works for numbers larger than 4, and not numbers with integer square roots
    """
    largest_prime = 0
    temp_num = int(sqrt(number))

    for x in range(2, temp_num+1):
        if number % x == 0:
            largest_prime = problem_3b(int(number/x))  # reached a possible prime number
            break
        if x == temp_num:
            largest_prime = number

    return largest_prime


def problem_3c(number):
    """
    Find the largest prime number (fast way, correction added for nums with integer square root)
    Works for numbers larger than 3
    """
    largest_prime = 0
    temp_num = int(sqrt(number))

    for x in range(2, temp_num+1):
        if number % x == 0:
            if number / x == x:  # if we increment up and reach integer sqrt, this is largest prime
                largest_prime = x
            else:
                largest_prime = problem_3c(int(number/x))  # reached a possible prime number
            break
        if x == temp_num:
            largest_prime = number

    return largest_prime


# print(problem_3c(13195))
print(problem_3c(47))
