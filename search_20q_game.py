import random

def game():
    x=random.randint(1,10000)
    for i in range(20):
        n=int(input('Enter Your Choice'))
        if x==n:
            print(f'You guessed the Number in {i+1}')
        elif x<n:
            print('Go Lower')
        else:
            print('Go Higher')

def compplay():
    print('Take a number a less than 100000')
    x=100000
    print()
    for i in range(1,20):
        print()
