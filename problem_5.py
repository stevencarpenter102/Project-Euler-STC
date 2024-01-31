from timeit import default_timer as timer
from sympy import *
import math

def smallest_num_divisible_by_1_to_20():
    """
    :return smallest positive number divisible by 1, 2, 3...20 (without a remainder)
    """
    smallest_num = 0
    found = False
    mod_is_zero = 0

    while(not found):
        smallest_num += 21
        for idx in range(1,21):
            if smallest_num % idx == 0:
               mod_is_zero += 1
            else:
                break
        if mod_is_zero == 20:
            found = True
        else:
            mod_is_zero = 0

    return smallest_num

def smallest_num_divisible_by_1_to_20_fast():
    """
    :return smallest positive number divisible by 1, 2, 3...20 (without a remainder)
    faster method than first attempt above
    for algorithm explaination see: https://projecteuler.net/overview=0005
    """
    smallest_num = 1

    for num in range(2,20):
        if isprime(num):
            prime_num_exponents = floor(math.log(20) / math.log(num))
            smallest_num *= num**prime_num_exponents

    return smallest_num 

start = timer()
print(smallest_num_divisible_by_1_to_20()) # 232792560 (correct!)
end = timer()
print("The 'slow' algorithm takes: ", round(end - start, 6), "sec") # Time in seconds, e.g. 5.38091952400282

start = timer()
print(smallest_num_divisible_by_1_to_20_fast()) # 232792560 (correct!)
end = timer()
print("The 'fast' algorithm takes: ", round(end - start, 6), "sec") # Time in seconds, e.g. 5.38091952400282