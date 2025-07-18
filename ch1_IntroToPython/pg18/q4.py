'''
convert from fahrenheit to celcius
'''

temp = 87

def fToC(f):
    return (5/9) * (f - 32)

print("Fahrenheit:", temp, "\nCelcius:", fToC(temp))