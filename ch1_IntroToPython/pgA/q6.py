'''
684 units of electricity in a month
electricity = 0.19 per unit  +  26.20
(units * 0.19) + 26.20
'''

units = int(input("Units? "))
price = (units * 19) + 2620

print(f"€{price//100}.{price%100:02d} per month")
