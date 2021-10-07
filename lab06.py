# 1. Name:
#     Devan Hoyt
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Search through a file efficently for a specified item
# 4. Algorithmic Efficiency
#      Currently my program is 0(log n^2) but I believe the efficency is 0(log n) or 0(n) when working. The size of the 
#      file would directly influence time of the program.
# 5. What was the hardest part? Be as specific as possible.
#      The biggest issue is getting the assignment to iterate through the search.
#       I tried with my original pseudocode(but changed to try and fix the issue)
#       but recieved the same issues and then I tried to start over and go with the
#       pseudocode provided in week 5 but am still recieving the same few errors.
#       I can detect if the file is empty, but it gets hung up when I get to the
#       search loop.
#       I figured the above issue out, I was reusing a variable from my pseudocode that
#       was different from when I redid the program. Now it is getting bogged in the loop and not exiting
# 6. How long did it take for you to complete the assignment?
#      6 hours roughly   

import json
#gets the file name
fileName = str(input("Please enter the file name"))
i_total = []
#open file
try:
    file = open(fileName, 'r')
    newFile = file.read()
    file.close()
    data_JSON = json.loads(newFile)
    data = data_JSON["array"]
    # for item in data["array"]:
    #     i_total.append(item)

    

    #prompt for word to search for
    search = input("What is the word you are searching for?")

    #decleration of variables
    i_first = 0
    i_last = len(data) - 1   
    #i_last = range(len(i_total) - 1)
    i_middle = int((i_first + i_last) // 2)
    print(i_middle)

    #if file is empty this detects it. 
    if i_last <= 0:
        print(f"{search} was NOT found in this file because the file is empty.")
        quit()

    found = False

    #searching loop. 
    while i_first <= i_last and found == False:
        
        if data[i_middle] == search:
            found = True
        elif data[i_middle] < search:
            i_first = i_middle + 1
            found = False
        else:
            i_last = i_middle - 1
            found = False
        # else:
        #     found = True

    # if found == true:
    #     print(f"{search} was found in this file.")
    if found:
        print(f"{search} was found in this file.")
    else:
        print(f"{search} was NOT found in this file")

except FileNotFoundError:
    print("Unable to open file")

# I tried doing the search outside of the try but got different errors then
# search = input("What is the word you are searching for?")

# i_first = 0
# i_last = len(data)
# #i_last = range(len(i_total))

# if i_last == 0:
#     print(f"{search} was NOT found in this file")
#     quit()

# found = False

# while i_first <= i_last and not found:
#     i_middle = (i_last + i_first) / 2

#     if i_total[i_middle] < search:
#         i_first = i_middle + 1
#     elif i_total[i_middle] > search:
#         i_last = i_middle - 1
#     else:
#         found = True

# if found == true:
#     print(f"{search} was found in this file.")

# else:
#     print(f"{search} was NOT found in this file")