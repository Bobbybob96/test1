"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1

cylinder1.py

Thomas Heine
100777741

"""
from math import pi

def volume_cylinder(diameter, height):
    """Volume of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be non-negative")
    return round(pi * (diameter / 2.0)**2 * height, 4)

def area_cylinder(diameter, height):
    """Surface area of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be non-negative")
    radius = diameter / 2.0
    return round(2.0 * pi * radius * (height + radius), 4)

if __name__ == "__main__":
    try:
        while True:
            dia = float(input("\nDiameter? "))
            high = float(input("Height? "))
            try:
                print("The volume is", volume_cylinder(dia, high))
                print("The area is", area_cylinder(dia, high))
            except ValueError:
                print("Please enter a positive value for height.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
