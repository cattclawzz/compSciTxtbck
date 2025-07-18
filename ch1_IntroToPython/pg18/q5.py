'''
convert from miles to kilometers - if it cost 900 euro per km how much would a flight to singapore cost?
'''

distance = 6991
costPerKm = 900

def mToKm(m):
    return m / 1.60935

print(f"At a cost of €{costPerKm}, a {distance} mile helicopter ride from Dublin to Singapore would cost €{round(mToKm(distance)*costPerKm, 2)}")