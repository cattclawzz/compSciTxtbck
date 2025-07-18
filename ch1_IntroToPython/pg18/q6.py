from math import pi
from random import randint

def volumeOfCylinder(height, radius):
    return pi * (radius*2) * height

height = randint(1,10)
radius = randint(1,10)
totalLiquid = randint(1000, 10000)

print(f"to carry {totalLiquid} litres of water you would need {totalLiquid//volumeOfCylinder(height, radius)} {height}x{radius}cm cylinders")