from random import randint

def weightOnTheMoon(x):
    return round(x / 0.165, 4)

weight = randint(1,100)

print(f"Something that weighs {weight}kg on Earth weighs {weightOnTheMoon(weight)}kg on the moon.")
