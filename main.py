# /usr/bin/python3
# Made by Marcus Cornes 2021

# Setup script
import random


# Print version
print("Virtual pet v1.0 unreleased\n")

# Ask for the name of your new pet
name = input("What is the name of your new pet? ")


# Success message
print(f"Congratulations! You adopted {name}!\n")



# Make a new definition
def YourPetIs():
    randomnum = random.randint(1, 4)

    if randomnum == 1:
        print(f"\n{name} is hungry!\n")
        yesorno = input("Do you want to feed it? Y/N ")
        if yesorno == "Y" or "y":
            print(f"{name} was successfully fed! ")
            pass
        elif yesorno == "N" or "n":
            print(f"You didn't feed {name}.")
        else:
            print("We didn't understand your question so we are going to take the answer as a no.")
            pass
    

    if randomnum == 2:
        print(f"\n{name} is thirsty!\n")
        yesorno = input("Do you want to give it water? Y/N ")
        if yesorno == "Y" or "y":
            print(f"{name} is no longer thirsty! ")
            pass
        elif yesorno == "N" or "n":
            print(f"You didn't give {name} a drink.")
        else:
            print("We didn't understand your question so we are going to take the answer as a no.")
            pass

        
    if randomnum == 3:
        print(f"\n{name} is tired!\n")
        yesorno = input("Do you want to make it sleep? Y/N ")
        if yesorno == "Y" or "y":
            print(f"{name} successfully went to sleep! ")
            pass
        elif yesorno == "N" or "n":
            print(f"{name} isn't going to sleep")
        else:
            print("We didn't understand your question so we are going to take the answer as a no.")
            pass


     
    if randomnum == 4:
        print(f"\n{name} needs cleaning!\n")
        yesorno = input("Do you want to clean it? Y/N ")
        if yesorno == "Y" or "y":
            print(f"You cleaned {name}!")
            pass
        elif yesorno == "N" or "n":
            print(f"{name} wasn't cleaned")
        else:
            print("We didn't understand your question so we are going to take the answer as a no.")
            pass


while True:
    YourPetIs()