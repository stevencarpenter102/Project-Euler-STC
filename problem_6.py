def sum_squared(end_integer):
    """
    sum of squares of each integer from [1, end_integer] is returned 

    end_integer -- should be positive number >= 1
    """
    sum = 0
    for x in range(1,end_integer+1):
        sum += x**2

    return sum

def square_sum(end_integer):
    """
    square of the sum of integers from [1, end_integer] is return

    end_integer -- should be positive number >= 1
    """
    sum = 0
    for x in range(1,end_integer+1):
        sum += x 

    return sum**2 


print(square_sum(100) - sum_squared(100))
