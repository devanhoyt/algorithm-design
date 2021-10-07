# 1. Name:
#      Devan Hoyt
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      read data from a file, convert to a json object, seperate username and password into seperate lists
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part about this was getting the passwords and usernames to match when searching for them in 
#       the indexs. Everything else was fairly simple, such as reading from the json and like that but I had to 
#       Try a few different things to get that to work correctly. 
# 5. How long did it take for you to complete the assignment?
#      2.5 hours from start to finish
import json

# opens and reads the json file into a variable, with except the case for failing.
try:
    with open('Lab02.json') as file:
        data = json.load(file)
        file.close()
except FileNotFoundError:
    print("Unable to open file Lab01.json")
# dataset = json.dumps(data)

users = data["username"]
passes = data["password"]

#This gets user inputs.
username = input("Username: ")
password = input("Password: ")

#Try statement that idexes the string into something to compare to.
try:
    index_user = users.index(username)
    index_pass = passes.index(password)

    if index_user == index_pass:
        print("You are Authenticated!")
    else:
        print("You are not authorized to enter the system")

#if neiher are correct this is the default.
except:
    print("You are not authorized to enter the system")