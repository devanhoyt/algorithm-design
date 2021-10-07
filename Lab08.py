# 1. Name:
#      Devan Hoyt
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This assignment is meant to read through a list of names and sort them
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was placing meaningful asserts. I don't know if it is getting easier
#      or if the pseudocde provided was easy to translate into code but the actual coding
#      only took 30-40 minutes. minor debugging and correct formating took a little but 
#      overall this was my most confident assignment yet.
# 5. How long did it take for you to complete the assignment?
#      2 hours

import json


file_prompt = input("Please enter the file name: ")
#Open the json file
try:
    file = open(file_prompt, 'r')
    new_file = file.read()
    file.close()
    data_JSON = json.loads(new_file)
    data = data_JSON["array"]

#error if fails
except FileNotFoundError:
    print("Unable to open file")

#counts objects in list
object_count = len(data)

i_pivot = object_count-1
assert i_pivot >= 0, "This list is empty, try again"

#loop through to check all items in list
while i_pivot > 0:

    i_largest = 0
    assert i_largest == 0, "i_largest did not start at 0"
    #compares items in the array
    for i_check in range(i_pivot +1):
        if data[i_check] > data[i_largest]:
            i_largest = i_check

        assert i_check < object_count, "i_check is less than the total amount of objects"
    #swaps items in list if one is greater than other
    if data[i_largest] > data[i_pivot]:
        data[i_largest], data[i_pivot] = data[i_pivot], data[i_largest]
        assert i_pivot > i_largest, "i_pivot must be larger than i_largest to swap"

    #way to exit loop
    i_pivot -= 1

#print the data in correct format
print(f"The values in {file_prompt} are: ")
x = '\n\t'.join(map(str, data))
print(f"\t{x}")