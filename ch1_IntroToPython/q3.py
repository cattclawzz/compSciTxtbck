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

def x(size): #fix this
    half = int(size //2)
    for i in range(half):
        print(f"{' '*i}\\{' '*(size-((i+1)*2))}/")

    if size%2 == 1:
        print(f"{'X':>{half+1}}")

    for i in reversed(range(half)):
        print(f"{' '*i}/{' '*(size-((i+1)*2))}\\")

face()
x(5)