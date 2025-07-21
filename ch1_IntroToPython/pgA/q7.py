'''
fish = 4.50
chips = 2.80
'''

fish = int(input('How many fish? '))
chips = int(input('How many chips? '))

total = (fish*450)+(chips*280)
total += int(total*.09)

print(f"€{total//100}.{total%100:02d}")