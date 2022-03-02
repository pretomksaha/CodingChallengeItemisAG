def takeInput():
    # take input values in list
    Items = []
    print('Give your input in line by line and exit with (done):')
    while True:
        status = input()
        if status == 'done':
            break
        else:
            Items.append(status)
    return Items

def findInput(location):
    with open(location) as line:
        programList =line.read().split('\n')
    return programList

def initialize():
    print('Do you want manual input?')
    myInput = input('Type yes or no:')
    try:
        if myInput == 'yes':
            myList=takeInput()
        elif myInput == 'no':
            myFile = input('Give the file location:')
            myList=findInput(myFile)
        return myList
    except:
        print('ERROR: Please Check your Inputs..')

