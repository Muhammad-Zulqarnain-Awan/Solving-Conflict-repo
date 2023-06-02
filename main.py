
def people(number):
    
    if number > 0:
        print("World Population: ",number)
    else:
        print("All are death. We are ghosts.")

number = int(input("Enter the number of population: "))
people(number)