timeStr = input("Time? ")
time = timeStr.split(':')
time = [int(i) for i in time]
mult = [3600, 60, 0]

print(f"{timeStr} in seconds is {sum([time[i]*mult[i] for i in range(3)])}")