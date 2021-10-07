# 1. Name:
#      Devan Hoyt
# 2. Assignment Name:
#      Lab 10: Fibonacci
# 3. Assignment Description:
#      This program is meant to calculate the nth number of the fibonocci sequence
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was ensuring calculations were correct and getting the school
#       loop to function correctly. I got confused from reading the announcements
#       and going off of what the assignment said, so I implemented
#       both versions of the sequence. I also spent time trying to change the school loop
#       to give the general answer which for this design involves changing fib_array to initialize 
#       with [0, 1]
# 5. How long did it take for you to complete the assignment?
#      Roughly 2 hours
import math

#Prompt to get the initial number sequence
num = int(input("Which Fibonacci number would you like to see? "))

#Asserts to ensure number is both not too large or small
assert num > -1, "Number must be positive"
assert num < 10000000, "Number is too large and may cause system failure."

#Positions 0 and 1 are 1 by default
if num < 2:
    fib = 1
#Loop to calculate the sequence number
else:
    #To change this way to the general way, change fib_array to initialize with [0, 1]
    fib_array = [1, 1]
    assert fib_array == [1, 1], "fib_array was wrongly initialized"
    for count in range(2, num + 1):
        fib_array[count % 2] = fib_array[0] + fib_array[1]
    fib = fib_array[num % 2]
    assert fib == fib_array[num % 2], "Fib was not stored correctly"


#Print statement defining the fib number(In red for the school way to make it clearer to see)
print(f"Fibonacci number {num} is \033[1;31;40m{fib}\033[0m for the school way")


#Binet's formula to calculate the fibonacci sequence
a = (1 + math.sqrt(5))/2
assert a == 1.618033988749895, "A was not calculated correctly"
b = a**num/math.sqrt(5)
c = round(b)

#Display for the general way is in green when displayed
print(f"For the general way, it is \033[1;32;40m{c}\033[0m")
