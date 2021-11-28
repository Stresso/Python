import random
global words
global hints
global word
global hang
guess = ''
global a
global b
a = ['', '', '', '', '', '', '']
b = ['H','A','N','G','M','A','N']
hang =-1

def initial():
    global temp_ans
    temp_ans = []
    for i in range(len(current)):
        temp_ans.append("_")


def question():
    print(f'{temp_ans}:{hints[word]}')


def update():
    pos = -1
    for i in current:
        pos += 1
        if i == guess:
            temp_ans[pos] = i


def player_guess(guess):
    guess = input(("Enter the guess:"))
    return guess.lower()


def check():
    global hang
    if guess not in current:
        hang+=1
        print(f"hang={hang}")
        wrong(hang)
    else:
        return


def hangman():
    print(
        f'''
__________________________________________
{a[0]}{a[1]}{a[2]}{a[3]}{a[4]}{a[5]}{a[6]}  
__________________________________________   
''')
    if hang == 6:
        print("You lose!")
        exit()
    else:
        global output
        output=''
        for i in temp_ans:
            output += i
        if output==current:
            print("You win")
            exit()

def wrong(hang):
    a[hang] = b[hang]


words = {
    1: 'privacy',
    2: 'sequence',
    3: 'function',
    4: 'source',
    5: 'matching'
}
hints = {
    1: 'keeping yourself and your personal information data safe when off and online',
    2: 'one of the 5 control structures in programming, which illustrates the importance of the order in which a set '
       'of operations is performed ',
    3: 'one of the 5 control structures in programming, where a useful set of operations is given a name, '
       'which is used to call the set of operations into action, wherever it is required. Returns a value',
    4: '(code) a program written in a high-level language before being compiled',
    5: 'patterns, in computer science, pattern matching is the act of checking a given sequence of tokens for the presence of the constituents of some pattern'
}
word = random.randint(3, 4)
current = words[word]
initial()
while True:
    question()
    guess = player_guess(guess)
    update()
    check()
    hangman()
