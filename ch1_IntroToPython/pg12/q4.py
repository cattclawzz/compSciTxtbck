'''
tldr: create a cross stitch pattern with Xs
'''
def checkers(x,y):
    for i in range(y):
        for j in range(x):
            if i%2 == j%2:
                print('XX', end='')
            else:
                print('  ', end='')
        print()

checkers(40,30)