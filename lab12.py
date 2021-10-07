# 1. Name:
#      Devan Hoyt
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      Display all prime numbers up to the Nth number as defined by the user.
# 4. What was the hardest part? Be as specific as possible.
#      I didn't understand the example pseudocode this week with making the array
#       full of booleans and then changing them to false when they weren't prime. 
#       However I also couldn't get my original pseudocode to work and kept getting 
#       syntax errors so I replicated the pseudocode provided as best as I could. 
# 5. How long did it take for you to complete the assignment?
#      About 3 hours overall

import math
import array as arr

#prompt for the prime numbers under N
n = int(input("This program will find all the prime numbers at or below N. Select that N: "))

assert n > 1, "N must be greater than 2"

numbers = [True] * n
#Need to add one more spot to numbers
numbers.append(True)

numbers[0] = False
assert numbers[0] == False, "The first item is needs to be false."


#changes the factor postion in numbers to false if not a prime number
for factor in range(2, int(math.sqrt(n)) + 1):
    if numbers[factor]:
        for multiples in range(factor * 2, n + 1, factor):
            numbers[multiples] = False

#initialize primes
primes = []

#ensures that 2 doesn't repeat when printing
if n < 3:
    primes.append(2)
    
#adds prime numbers to the primes
for index in range(2, n):
    if numbers[index]:
        primes.append(index)

assert numbers != [], "The numbers array is empty"
print(f"The prime numbers at or below {n} are {primes}")


#Alternate way to do this that I worked on with a tutor.

# numbers = []
# n = int(input("This program will find all the prime numbers at or below N. Select that N: "))


# numbers.extend(range(2,n + 1))

#


# factor = 2

# for factor in range(2, int(math.sqrt(n)) + 1):
  
#     if factor in numbers:
         
#         for nonprime in range(factor * 2, n + 1, factor):
            
#             if nonprime in numbers:
#                 numbers.remove(nonprime)
    
    
#     factor += 1



# print(f"The prime numbers at or below {n} are {numbers}")