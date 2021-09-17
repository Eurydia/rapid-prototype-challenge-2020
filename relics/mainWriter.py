from mainRef import fields, fieldNames, fieldLen


messageLiteral = []


messageBin = []


choiceDec = []


def display_question(num, name, list, valuemin, valuemax):

    print(f'\n{num}. select {name.title()}')

    for items in range(0, len(list)):

        choiceItem = f'|\t{items}. {list[items].title()}'

        print(choiceItem)

    picked = int(input(f'\nselect index (from {valuemin} to {valuemax}): '))

    return picked


def output(num, name, list, picked, **kwargs):

    print(f'\t*{list[picked].title()}* selected for {name}')

    pickedBinary = bin(picked)[2:]

    expectedLen = fieldLen[num]

    while expectedLen > len(pickedBinary):
            pickedBinary = f'0{pickedBinary}'

    kwargs['outBin'].append(pickedBinary)

    kwargs['outDec'].append(picked)

    kwargs['outLiteral'].append(list[picked])

    print('-' * 100)


def question(num, name, list, **kwargs):


    indexMin = list.index(list[0]) if kwargs['min'] == None else kwargs['min']

    indexMax = list.index(list[-1]) if kwargs['max'] == None else kwargs['max']


    choiceSelected = display_question(num, name, list, indexMin, indexMax)

    while not indexMax >= choiceSelected >= indexMin:

        print('\n\tError IndexOutOfRange\n')

        print('-' * 100)

        choiceSelected = display_question(num, name, list, indexMin, indexMax)

    output(num, name, list, choiceSelected, outDec=choiceDec, outBin=messageBin, outLiteral=messageLiteral)

    return choiceSelected


def question_m(toget, min, max, exptLen):

    print(f'\n\t {toget}')

    choiceSelected = int(input(f'Enter {toget} (from {min} to {max}): '))

    while not max >= choiceSelected >= min:
        print('\n\tError IndexOutOfRange\n')

        print('-' * 100)

        print(f'\n\t {toget}')

        choiceSelected = int(input(f'Enter {toget} (from {min} to {max}): '))

    print(f'\t*{choiceSelected}* selected for {toget}')

    choiceBinary = bin(choiceSelected)[2:]

    while exptLen > len(choiceBinary):
        choiceBinary = f'0{choiceBinary}'

    return choiceBinary, choiceSelected


def question_a(toget, num, name, min, max, digitx):

    print(f'\n{num}. select {name.title()}')

    choiceSelected = float(input(f'Enter {toget} (from {min}{digitx} to {max}{digitx}): '))

    while not max >= choiceSelected >= min:
        print('\n\tError IndexOutOfRange\n')

        print('-' * 100)

        print(f'\n{num}. select {name.title()}')

        choiceSelected = float(input(f'Enter {toget} (from {min}.{digitx} to {max}.{digitx}): '))

    print(f'\t*{choiceSelected}* selected for {name}')

    print('-' * 100)

    return choiceSelected


def question_a_c(num, order, choice):
    choiceBinary = bin(order)[2:]

    expectedLen = fieldLen[num]

    while expectedLen > len(choiceBinary):
        choiceBinary = f'0{choiceBinary}'

    messageBin.append(choiceBinary)

    choiceDec.append(choice)

    messageLiteral.append(str(choice))



def writeMessage(index):

    n, k, p = '.000', '', '.00'

    key = fields[index]

    idenTitle = fieldNames[index]

    if index == 3:

        keyA0 = fields[index + 1]

        print(f'\n{index}. select {idenTitle.title()}')

        for items in range(0, len(key)):
            choiceItem = f'|\t{items}. {key[items].title()}'

            print(choiceItem)

        valuemin = key.index(key[0])
        valuemax = key.index(key[-1])

        picked = int(input(f'\nselect index (from {valuemin} to {valuemax}): '))

        while not valuemax >= picked >= valuemin:

            print('\n\tError IndexOutOfRange\n')

            print('-' * 100)

            print(f'\n{index}. select {idenTitle.title()}')

            for items in range(0, len(key)):
                choiceItem = f'|\t{items}. {key[items].title()}'

                print(choiceItem)

            picked = int(input(f'\nselect index (from {valuemin} to {valuemax}): '))

        print(f'\t*{key[picked]}* selected for {idenTitle}')

        print('-' * 100)

        print(f'\t items in {key[picked]}')

        for items in range(0, len(keyA0[picked])):
            choiceItem = f'|\t{items}. {keyA0[picked][items].title()}'

            print(choiceItem)

        confirm = int(input('Are you sure? (1/0): '))

        print('-' * 100)

        while confirm == 0:

            print(f'\n{index}. select {idenTitle.title()}')

            for items in range(0, len(key)):
                choiceItem = f'|\t{items}. {key[items].title()}'

                print(choiceItem)

            valuemin = key.index(key[0])
            valuemax = key.index(key[-1])

            picked = int(input(f'\nselect index (from {valuemin} to {valuemax}): '))

            while not valuemax >= picked >= valuemin:

                print('\n\tError IndexOutOfRange\n')

                print('-' * 100)

                print(f'\n{index}. select {idenTitle.title()}')

                for items in range(0, len(key)):
                    choiceItem = f'|\t{items}. {key[items].title()}'

                    print(choiceItem)

                picked = int(input(f'\nselect index (from {valuemin} to {valuemax}): '))

            print(f'\t*{key[picked]}* selected for {idenTitle}')

            print('-' * 100)

            print(f'\t items in {key[picked]}')

            for items in range(0, len(keyA0[picked])):
                choiceItem = f'|\t{items}. {keyA0[picked][items].title()}'

                print(choiceItem)

            confirm = int(input('Are you sure? (1/0): '))

            print('-' * 100)

        pickedBinary = bin(picked)[2:]

        expectedLen = fieldLen[index]

        while expectedLen > len(pickedBinary):
            pickedBinary = f'0{pickedBinary}'

        messageBin.append(pickedBinary)

        choiceDec.append(picked)

        messageLiteral.append(key[picked])

    elif index == 4:

        keyA0 = int(choiceDec[index - 1])

        keyA1 = key[keyA0]

        idenName = f'{idenTitle} ({fields[index - 1][keyA0]})'

        question(index, idenName, keyA1, min=None, max=None)

    elif index == 6:

        print(f'\n{index}. select {idenTitle.title()}')

        dayBin, dayDec = question_m('day', 0, 31, 5)

        hourBin, hourDec = question_m('hour', 0, 24, 5)

        minuteBin, minuteDec = question_m('minute', 0, 59, 6)

        choiceDec.append([dayDec, hourDec, minuteDec])

        choiceBin = f'{dayBin}{hourBin}{minuteBin}'
        messageBin.append(choiceBin)

        choiceSelected = f'day {dayDec} hour {hourDec} minute {minuteDec}'
        messageLiteral.append(choiceSelected)

        choiceSelectedT = f'\t*{choiceSelected}* selected for {fieldNames[index]}'

        print(choiceSelectedT)

        print('-' * 100)

    elif index == 11:
        x = n

        latChoice = question_a('latitude', index, idenTitle, -90, 90, x)

        latOrder = int((latChoice + 90)/0.0027466)

        question_a_c(index, latOrder, latChoice)


    elif index == 12:
        x = n

        longChoice = question_a('longitude', index, idenTitle, -180, 180, x)

        longOrder = int((longChoice + 180)/0.0027466)

        question_a_c(index, longOrder, longChoice)

    elif index == 15:
        x = p

        aziChoice = int(question_a('azimuth', index, idenTitle, 0, 180, x))

        aziOrder = int(aziChoice / 5.806)

        question_a_c(index, aziOrder, aziChoice)

    else:

        question(index, idenTitle, key, min=None, max=None)


for i in range(17):
    writeMessage(i)


print(''.join(messageBin))

print(messageLiteral)


