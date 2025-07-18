'''
Using ordinary characters and special charachters, write the code to create a pattern in the shape of
a face
the letter x
a triangle
a small circle
and a larger circle
'''
from math import sqrt

def face():
    print(':)')

def x(size):
    half = size//2
    for i,j in zip(range(half),range(size-2,-2,-2)):
        print(f"{' '*i}\\{' '*j}/")
    
    if size%2 == 1:
        print(f"{'X':>{half+1}}")

    for i,j in zip(range(half-1,-1,-1),range(0+(size%2),(half*2)+2+(size%2),2)):
        print(f"{' '*i}/{' '*j}\\")

def triangle(size):
    for i,j in zip(range(size-1,0,-1),range(0,(size+1)*2,2)):
        print(f"{' '*i}/{' '*j}\\")
    print(f"/{'_'*(size-1)*2}\\")

def circle(diameter):
    if diameter % 1 == 1:
        diameter += 1
    mid = (diameter // 2)
    for x in range(diameter):
        for y in range(diameter):
            distance = sqrt( (abs(x-mid)**2) + (abs(y-mid)**2))
            if distance <= diameter//2:
                print('* ', end='')
            else:
                print('  ', end='')
        print()

face()
print()
x(8)
print()
triangle(5)
print()
circle(7)
print()
circle(19)