import math

def is_prime(num):
    """
    return true if num is prime
    """
    isPrime = True
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            isPrime = False
            break

    return isPrime

def prime_number_nth(n):
    """
    returns the 'nth' prime number (first six prime numbers are: 2, 3, 5, 7, 11 & 13)
    """
    found = False    # found the 'nth' prime number user is asking to find
    prime_nums_found = 0
    next = 2

    while(found != True):
        if is_prime(next):
            prime_nums_found += 1

        if prime_nums_found == n:
            found = True
        else:
            next += 1

    return next

# print(prime_number_nth(6)) # ANSWER ----> 13
print(prime_number_nth(10001))