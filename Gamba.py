import random

num = 0
guess = 0
bal = 1000
while True:
    if bal==0:
        print('You ran out of money')
        exit()

    choice=input('''
enter your choice:
1 for 0.5x
2 for 2x
3 for 5x
4 for 10x
5 for Quit
''')

    if choice=='5':
        print(f'You left the casino with {bal}')
        exit()
    bet=input(f'How much will you bet? Max({bal}):')
    bet=int(bet)
    bal-=bet
    if choice=='1':
        num=input('Enter a number between 1-2:')
        guess=random.randint(1,2)
        print(guess)
        if guess==int(num):
            print(f'You win ${bet*0.5}')
            win= bet*0.5
            print(f'balance:${bal+win+bet}')
        else:
            print(f'You lost ${bet}')
            print(f'balance:${bal}')
    elif choice=='2':
        num=input('Enter a number between 1-3:')
        guess=random.randint(1,3)
        print(guess)
        if guess==int(num):
            print(f'You win ${bet*2}')
            win= bet*2
            print(f'balance:${bal+win+bet}')
        else:
            print(f'You lost ${bet}')
            print(f'balance:${bal}')
    elif choice=='3':
        num=input('Enter a number between 1-4:')
        guess=random.randint(1,4)
        print(guess)
        if guess==int(num):
            print(f'You win ${bet*5}')
            win= bet*5
            print(f'balance:${bal+win+bet}')
        else:
            print(f'You lost ${bet}')
            print(f'balance:${bal}')
    elif choice=='4':
        num=input('Enter a number between 1-5:')
        guess=random.randint(1,5)
        print(guess)
        if guess==int(num):
            print(f'You win ${bet*10}')
            win= bet*10
            print(f'balance:${bal+win+bet}')
        else:
            print(f'You lost ${bet}')
            print(f'balance:${bal}')
