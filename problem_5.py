def smallest_num_divisible_by_1_to_20():
    """
    :return smallest positive number divisible by 1, 2, 3...20 (without a remainder)
    """
    smallest_num = 0
    found = False
    mod_is_zero = 0

    while(not found):
        smallest_num += 20
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
    """
    list = []
    for idx in range(1,20):
        list = list + [idx]

    return list 

def gcd(a, b):
    """
    Computes the greatest common divisor of two integers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b   # 21, 7 -> # 7, 0
    return a

# print(smallest_num_divisible_by_1_to_20()) # 232792560 (correct!)
print(gcd(49, 21))
# print(smallest_num_divisible_by_1_to_20_fast()) 

