'''
Using ordinary characters and special charachters, write the code to create a pattern in the shape of
a face
the letter x
a triangle
a small circle
and a larger circle
'''

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

def circle():
    pass

face()
print()
x(8)
print()
triangle(5)
print()