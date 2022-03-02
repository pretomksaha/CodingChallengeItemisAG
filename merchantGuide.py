import inputList
def valueAssassin(iteminList):
    'Function to assign credit to the metal according Roman Letter.'
    'Input:'
    'iteminList: List of Metals'
    'Output:'
    'result: List of metal and their credits'
    valueList = {}
    shortList = [num for num in iteminList if len(num) ==2]
    findValue= [num for num in iteminList if num[-1].isdigit()]
    itarateValue = [num for num in iteminList if ((len(num) > 2) and not (num[-1].isdigit()))]
    result= []
    for item in shortList:
        if item[1] == 'I':
            valueList[str(item[0])] = 1
        elif item[1] == 'V':
            valueList[str(item[0])] = 5
        elif item[1] == 'X':
            valueList[str(item[0])] = 10
        elif item[1] == 'L':
            valueList[str(item[0])] = 50
        elif item[1] == 'C':
            valueList[str(item[0])] = 100
        elif item[1] == 'D':
            valueList[str(item[0])] = 500
        elif item[1] == 'M':
            valueList[str(item[0])] = 1000
        else:
            print('Please, Check your Input!..')

    for items in findValue:
        for item in items:
            if valueList.get(item) is not None:
                   items[items.index(item)] = valueList.get(item)

    for list in findValue:
        finalvalue, itemname = searchValue(list)
        valueList[str(itemname)] = finalvalue

    for items in itarateValue:
        for item in items:
            if valueList.get(item) is not None:
                   items[items.index(item)] = valueList.get(item)

    for list in itarateValue:
        finalvalue = calculateCredit(list)
        result.append(finalvalue)
    return result

def calculateCredit(CreditList):
    'Function to calculate the credits for the questions in the input list.'
    'input:'
    'CreditList: List of metal which has assign credit and non assign combinations'
    'output:'
    'finalValue: calculated credits for every metal and question.'
    sum = CreditList[0]
    compareList=[1,10,100,1000]
    lastvalue = CreditList[0]
    finalValue = 0
    flag = False
    count=0
    for i in range(1, len(CreditList)):
        if (int(CreditList[i]) == lastvalue) and ((int(CreditList[i]) in compareList)):
            sum = int(CreditList[i])+sum
            lastvalue = int(CreditList[i])
            if i == len(CreditList)-1:
                finalValue= sum
            elif count > 2:
                print('Please, Check your Input!..')
            else:
                count=count+1
                flag = True
        else:
            if (int(CreditList[i]) > lastvalue):
                if (flag == True) and (count <2):
                    finalValue = (int(CreditList[i])*lastvalue)/2-sum
                    flag =False
                    count = 0
                if (flag == True) and (count >= 2):
                    print('Please, Check your Input!..')
                else:
                    sum = int(CreditList[i]) - sum
                    lastvalue = int(CreditList[i])
                    finalValue = sum
            elif (int(CreditList[i]) < lastvalue)and (count <2):
                if flag == True:
                    finalValue =sum-int(CreditList[i])
                    flag =False
                    count = 0
                if (flag == True) and (count >= 2):
                    print('Please, Check your Input!..')
                else:
                    sum = int(CreditList[i]) + sum
                    lastvalue = int(CreditList[i])
                    finalValue = sum
            else:
                print('Please, Check your Input!..')
    return finalValue

def searchValue(findValue):
    'Function to search credit for non assign metal.'
    'Input:'
    'findValue: list of Metal and credit'
    'Output:'
    'finalValue: Final credit for every available metal '
    'itemName: List of the metal'
    sum=0
    lastvalue=findValue[0]
    finalValue=0
    flag=False
    for i in range(1,len(findValue)-2):
        if (int(findValue[i]) == lastvalue):
            lastvalue= int(findValue[i])
            sum=int(findValue[i])+lastvalue + sum
            flag=True
        elif (int(findValue[i]) > lastvalue):
            sum =int(findValue[i]) - lastvalue + sum
            lastvalue = int(findValue[i])
        elif (int(findValue[i]) < lastvalue):
            sum = int(findValue[i]) + lastvalue + sum
            lastvalue = int(findValue[i])
        else:
            print('Please, Check your Input!..')
    if flag == True:
        finalValue = (2 * (int(findValue[-1]) + sum))/lastvalue
    else:
        finalValue = int(findValue[-1]) + sum

    itemName=findValue[-2]

    return finalValue, itemName


def separateConditions(ListOfline):
    'Function to separate condition according their structure.'
    'Input:'
    'ListOfline: contain the input conditions and question'
    'Output:'
    'listWithValue: assign credits for sell metals and dirt '
    ' outputList: only have the question and  non logical line.'
    listWithValue = []
    outputList=[]
    for line in ListOfline:
        if 'is' in line:
            listOfWords = line.split(' ')
            if listOfWords[-1] == '?':
                if 'how much' in line or 'how many' in line:
                    listWithValue.append(listOfWords[listOfWords.index('is')+1:listOfWords.index('?')])
                    outputList.append(listOfWords[2:listOfWords.index('?')])
                else:
                    listWithValue.append('N')
                    outputList.append('N')
            elif len(listOfWords) < 4:
                listOfWords.pop(listOfWords != 'is')
                listWithValue.append(listOfWords)
            elif listOfWords[-1] == 'Credits':
                listOfWords.pop(listOfWords.index('is'))
                listOfWords.pop(listOfWords.index('Credits'))
                listWithValue.append(listOfWords)
            else:
                print('Here')
        else:
            listWithValue.append('N')
            outputList.append('N')

    return listWithValue, outputList

def initialize():
    'Function that initialize the mercants guide problem.'
    i=0
    showResult=[]
    print('\t\tProblem 3: MERCHANT\'S GUIDE TO THE GALAXY')
    programList = inputList.initialize()
    print('Inputs')
    print('\n'.join(programList))
    iteminlist, outputList = separateConditions(programList)
    resultCredits=valueAssassin(iteminlist)
    for eachList in outputList:
        if eachList =='N':
          showResult.append('I have no idea what you are talking about')
        else:
            if eachList[0]=='is':
                result=' '.join(eachList[1:])
                showResult.append(' '.join([result,str(eachList[0]),str(resultCredits[i])]))
                i = i + 1

            else:
                result=' '.join(eachList[2:])
                showResult.append(' '.join([result,str(eachList[1]),str(resultCredits[i]),str(eachList[0])]))
                i = i + 1
    print('\nOutputs: ')
    print('\n'.join(showResult))
