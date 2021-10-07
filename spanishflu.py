low_exp = 100
high_exp = 0
low_country = ""
high_country = ""

with open("life-expectancy.csv") as flu_file:
    for line in flu_file:
        new_line = line.strip()
        partial = new_line.split(",")
        country = partial[0]
        abrev = partial[1]
        year = partial[2]
        life_exp = partial[3]

        if(life_exp > high_exp):
            high_exp = life_exp
            high_country = parts[0]
        if(life_exp < low_exp):
            low_exp = life_exp
            low_country = parts[0]


print("Succesfull running file")        
user_year = input("Enter the year of interest: ")
print()
print(f"The overall max life expectancy is : {high_exp} from {high_country} in {year}")
print(f"The overall min life expectancy is: {low_exp} from {low_country} in {year}")

print(f"For the year{user_year}:")
print(f"The average life expectancy across all countries was {year}")
print(f"The max life expectancy was in {year} with {year}")
print(f"the min life expectancy was in {year} with {year}")