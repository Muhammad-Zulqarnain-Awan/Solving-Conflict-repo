
def people(number):
    
    if number > 0:
        return ("World Population: ",number)
    else:
        return ("All are death. We are ghosts.")

number = int(input("Enter the number of population: "))

print(people(number))