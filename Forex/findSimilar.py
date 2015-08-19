from shapeComparison import comparePattern
import settings

def findSimilar(currentPattern, pastData, predictionDistance, reqCloseScore, methodNumber):
                                                #takes a pattern and checks past data,
                                                #returns list of previous pattern start points in past data and 'pattern closeness score'
    patternLength = len(currentPattern)
    similarPatternsIndex = []
    
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

