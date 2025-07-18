'''
create a variable to store the value of your age. Assign the value of your age to the variable and display it with the following text: "What a great age!"
'''
import datetime

def getAge(DOB):
    return (datetime.datetime.now() - DOB).days // 365

age = getAge(datetime.datetime(2009, 3, 7))
print(f"{age}, What a great age!")