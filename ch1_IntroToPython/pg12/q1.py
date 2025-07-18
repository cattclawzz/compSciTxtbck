'''
Using two print() functions, write and test the code to display two print functions to display the string "Goodbye!" twice on the same line.
'''

def printMulti(string, amount):
    for i in range(amount):
        print(string, end='')
    print() #blankline to prevent future prints from ending up on the same line

printMulti('Goodbye!', 2)