import math

n = int(input("This program will find all the prime numbers at or below N. Select that N: "))

assert n > 1, "N must be greater than 2"

numbers = []
numbers.extend(range(2,n + 1))


#print(numbers)

factor = 2
for factor in range(2, int(math.sqrt(n)) + 1):
    if factor in numbers:
        for nonprime in range(factor * 2, n + 1, factor):
            if nonprime in numbers:
                numbers.remove(nonprime)
    factor += 1



print(f"The prime numbers at or below {n} are {numbers}")

