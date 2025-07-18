from random import randint

def avgRemPow(a,b):
    print('numbers:                 \t', a,b)
    print('Average:                 \t', (a+b)/2)
    print('Remainder after division:\t', a%b)
    print('First ^ the second:      \t', a**b)

avgRemPow(float(randint(1,100)), float(randint(1,100)))