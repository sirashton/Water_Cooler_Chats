import ast
from random import randrange
from random import uniform

#takes a list of filepaths of which children settings files will be made
def generateChildSettings(listOfFilepaths):

    parentSettings = []
    for i in listOfFilepaths:
        infile = open(i)
        parent = ast.literal_eval(infile.read())
        parentSettings.append(parent)

    baseFilepath = 'Settings/1'
    numberChildren = 10
    childrenMade = 0
    noVariablesChange = 2
    varsToChnage = []
    evolveSettings = [      #[change? 1yes0no, lowerLimit, upperLimit]
        [1, 2, 10], #futureDistance
        [0], #currentPatternIndex
        [1, 5, 15], #patternLength
        [0], #closeMethodNumber
        [0], #decideMethodNumber
        [1, 0, 100], #reqCloseScore
        [1, 5, 100], #reqNoSimilar
        [1, 0.001, 0.1]#reqAverageChange
                    ]
    
    while childrenMade < numberChildren:
        change = varsToChange(evolveSettings,noVariablesChange)
        childSettings = parentSettings[0][:]
        for i in change:
            childSettings[i] = makeSetting(i, parentSettings, evolveSettings)
        childrenMade += 1
        print(childSettings)
        outFilepath = str(baseFilepath + '.' + str(childrenMade) + '.txt' )
        outfile = open(outFilepath ,'w')
        outfile.write(str(childSettings))
        outfile.close()

def varsToChange(evolveSettings, noVariablesChange):

    possibleSettings = []
    
    for i in evolveSettings:
        if i[0] == 1:
            possibleSettings.append(evolveSettings.index(i))

    if len(possibleSettings) <=  noVariablesChange:
        return possibleSettings
    
    numberPicked = 0
    varsToChange = []
    while numberPicked < noVariablesChange:

        randIndex = randrange(0, len(possibleSettings))
        x = possibleSettings[randIndex]
        while x in varsToChange:
            randIndex = randrange(0, len(possibleSettings))
            x = possibleSettings[randIndex]
        varsToChange.append(x)
        numberPicked += 1

    return varsToChange

def makeSetting(index, parents, evolveSettings):
    parentSettings = []
    for i in parents:
        parentSettings.append(i[index])
    limits = evolveSettings[index][1:3]
    '''print(index)
    print(evolveSettings[index])
    print(limits)'''
    parentRange = float(max(parentSettings) - min(parentSettings))
    randomChange = (uniform(-0.1, 0.1))*(limits[1] - limits[0])
    randomChangeInherit = (uniform(-1,2))*parentRange
    newSetting = min(parentSettings) + randomChange
    while (newSetting < limits[0]) or (newSetting > limits[1]):
        randomChangeInherit = (uniform(-1,2))*parentRange
        randomChange = (uniform(-0.1, 0.1))*(limits[1] - limits[0])
        newSetting = min(parentSettings) + randomChangeInherit + randomChange
    return newSetting
