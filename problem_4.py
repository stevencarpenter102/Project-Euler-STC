def extract_digits_from_base_10_num(num):
    """
    :param num: a base-10 number
    :return: a list of digits (0-9) that compose the number (example: "8467" (base-10) -> [8, 4, 6, 7]
    """
    x = num
    y = 0
    list_of_digits = []
    list
    while not (x == 0):
        y = x % 10   # least significant digit in x
        list_of_digits.insert(0, int(y))
        x = (x - y) / 10

    return list_of_digits

def is_a_palindrome(potential_palindrome):
    """
    :param potential_palindrome: base-10 number that might be a palindrome
    :return: true means it is a palindrome
    """
    list_of_digits = extract_digits_from_base_10_num(potential_palindrome)

    while len(list_of_digits) >= 2 and list_of_digits[0] == list_of_digits[-1]:
        del list_of_digits[0]
        del list_of_digits[-1]

    length = len(list_of_digits)
    if length == 0 or length == 1:
        return True
    else:
        return False


def largest_palindrome_of_two_3_digit_nums():
    num2 = 999   # largest 3 digit number
    product = 0
    found = False
    potential_largest_palindromes = []
    largest_palindrome = 0

    for num1 in range(999, 1, -1):
        while not found and num2 > 1:
            num2 -= 1
            product = num1 * num2
            found = is_a_palindrome(product)
            if found:
                print(num1, num2, product)

        found = False
        num2 = num1
        potential_largest_palindromes.append(int(product))
        # print("Inner loop complete")

    potential_largest_palindromes.sort()
    if len(potential_largest_palindromes) >= 1:
        largest_palindrome = potential_largest_palindromes[-1]

    return largest_palindrome


# print(extract_digits_from_base_10_num(8467))
# print(is_a_palindrome(729316))
print("Largest palindrome is:", largest_palindrome_of_two_3_digit_nums())
