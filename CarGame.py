com=''
started = False
while True:
    com = input('Enter the command:')
    if com.lower()=="start":
        if not started:
            print('Car has started')
            started=True
        else:
            print('Car has been already started')

    elif com.lower()=='stop':
        if started:
            print('Car has stopped')
            started=False
        else:
            print('Car has been already stopped')

    elif com.lower()=='help':
        print('''
1)"start"
2)"stop"
3)"help"
4)"quit"
''')

    elif com.lower()=='quit':
        print('Thank you')
        exit()



