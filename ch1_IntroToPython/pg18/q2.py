from random import randint

def sumDiffProd(a,b):
    print('numbers:\t', a,b)
    print('sum:    \t', a+b)
    print('difference:\t', abs(a-b))
    print('product:\t', a*b)

sumDiffProd(float(randint(1,100)), float(randint(1,100)))