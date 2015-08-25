from dataProcessing import makeHistoricData
import ast


'''
settingsList =
    0  futureDistance
    1  currentPatternIndex
    2  patternLength
    3  closeMethodNumber
    4  decideMethodNumber
    5  reqCloseScore
    6  reqNoSimilar
    7  reqAverageChange
    
'''

def init(filepath):

    infile = open(filepath)

    settingsList = ast.literal_eval(infile.read())

    print(settingsList)
    
    global futureDistance
    futureDistance = int(settingsList[0])
    
    global historicData
    historicData = makeHistoricData()

    global currentPatternIndex
    currentPatternIndex = int(settingsList[1])

    global patternLength
    patternLength = int(settingsList[2])

    global currentPattern
    currentPattern = historicData[currentPatternIndex : currentPatternIndex + patternLength]

    global closeMethodNumber
    closeMethodNumber = settingsList[3]

    global decideMethodNumber
    decideMethodNumber = settingsList[4]
    
    global reqCloseScore
    reqCloseScore = settingsList[5]

    global reqNoSimilar
    reqNoSimilar = int(settingsList[6])

    global reqAverageChange
    reqAverageChange = settingsList[7]

    print('Settings initialised.')    

'''class globalSettings(object):
    currentPatternIndex = -5500'''
