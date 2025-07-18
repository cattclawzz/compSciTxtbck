from random import randint

def area(x,y):
    return x*y

length = randint(1,100)
width = randint(1,100)

houseLen = randint(1,length)
houseWid = randint(1,width)

lawnArea = area(width,length)-area(houseWid,houseLen)

mowingSpeed = 2

print(f"The area of a {width}x{length}m garden excluding a {houseLen}x{houseWid}m house is {lawnArea}m^2")
print(f"To cut the grass of the lawn at a rate of {mowingSpeed}m^2 per second, it would take you {round(mowingSpeed*(lawnArea/60), 2)} minutes")