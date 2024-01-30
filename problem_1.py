def problem_1():
    sum = 0
    for x in range(0, 1000):
        if x % 5 == 0 or x % 3 == 0:
            sum += x
    return sum


sum = problem_1()
print(sum)