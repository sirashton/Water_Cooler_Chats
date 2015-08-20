from dataProcessing import makeHistoricData

def init():
    global futureDistance
    futureDistance = 5
    
    global historicData
    historicData = makeHistoricData()

    '''global currentPatternIndex
    currentPatternIndex = -5500'''

    global patternLength
    patternLength = 10

    '''global currentPattern
    currentPattern = historicData[currentPatternIndex : currentPatternIndex + patternLength]'''

    global closeMethodNumber
    closeMethodNumber = 1

    global decideMethodNumber
    decideMethodNumber = 1
    
    global reqCloseScore
    reqCloseScore = 30

'''class globalSettings(object):
    currentPatternIndex = -5500'''
