fib_seq = [1,2]  # initial condition

def problem_2():
    sum = 0
    # fill list with fib seq up to 4 million
    while fib_seq[-1] < 4000000:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    del fib_seq[-1]

    # iterate over the fib sequence to add together the even-values terms
    for element in fib_seq:
        if element % 2 == 0:
            sum += element
    return sum


print(problem_2())
