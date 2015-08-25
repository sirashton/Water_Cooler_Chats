from shapeComparison import comparePattern
import settings

def findSimilar(currentPatternIndex):
                                                #takes a pattern and checks past data,
                                                #returns list of previous pattern start points in past data and 'pattern closeness score'
    reqCloseScore = settings.reqCloseScore
    methodNumber = settings.closeMethodNumber
    predictionDistance = settings.futureDistance
    historicData = settings.historicData
    similarPatternsIndex = []
    pastData = settings.historicData
    patternLength = settings.patternLength
    currentPattern = historicData[currentPatternIndex : currentPatternIndex + patternLength]
    
    for startPoint in range( 0 , len(pastData) - predictionDistance - patternLength):

        patternToCheck = pastData[startPoint : (startPoint + patternLength)]
        #print(str(startPoint))
        #print('toCheck : ' + str(len(patternToCheck)))
        #print('current : ' + str(len(currentPattern)))
        closeScore = comparePattern(currentPattern, patternToCheck, methodNumber)
        if closeScore > reqCloseScore:
            if closeScore != 100:
                similarPatternsIndex.append( [startPoint , closeScore] )
    return similarPatternsIndex

def findSimilarLive(pattern):
                                                #takes a pattern and checks past data,
                                                #returns list of previous pattern start points in past data and 'pattern closeness score'
    reqCloseScore = settings.reqCloseScore
    methodNumber = settings.closeMethodNumber
    predictionDistance = settings.futureDistance
    historicData = settings.historicData
    similarPatternsIndex = []
    pastData = settings.historicData
    patternLength = settings.patternLength
    currentPattern = pattern
    
    for startPoint in range( 0 , len(pastData) - predictionDistance - patternLength):

        patternToCheck = pastData[startPoint : (startPoint + patternLength)]
        #print(str(startPoint))
        #print('toCheck : ' + str(len(patternToCheck)))
        #print('current : ' + str(len(currentPattern)))
        closeScore = comparePattern(currentPattern, patternToCheck, methodNumber)
        if closeScore > reqCloseScore:
            if closeScore != 100:
                similarPatternsIndex.append( [startPoint , closeScore] )
    return similarPatternsIndex

