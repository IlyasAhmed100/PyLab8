# Task 8.1

# Importing
from math import pi

# Defining Main
def main():
    radius_circle = int(input("Type in a value for the radius of a circle" '\n'))
    print("You have chosen a radius of " + str(radius_circle) + " cm.")
    print("Your total area is ",area_of_circle(radius_circle), "cm^2")

# Defining area of circle
def area_of_circle(radius):
    area = pi * (radius ** 2)
    return area

main()
          
    
