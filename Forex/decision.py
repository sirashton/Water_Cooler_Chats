#Takes the current pattern, looks at past data, returns only, (buy, sell or hold)
import settings
from functools import reduce

from shapeComparison import percentageChange

def decide(similarPatternIndex):

    decideMethodNumber = settings.decideMethodNumber
    reqAverageChange = settings.reqAverageChange
    reqNoSimilar = settings.reqNoSimilar
    
    if decideMethodNumber == 1:
        if len(similarPatternIndex) > reqNoSimilar:
            futurePercentageChanges = futurePercentChanges(similarPatternIndex)
            futurePercentageChanges.sort()
            #print(str(futurePercentageChanges))

            averageFuturePercentageChange = reduce(lambda x, y: x + y, futurePercentageChanges) / len(futurePercentageChanges)
            print(averageFuturePercentageChange)
            if averageFuturePercentageChange > reqAverageChange:
                return 'BUY'
            elif averageFuturePercentageChange < -reqAverageChange:
                return 'SELL'
            else:
                return'HOLD'
        else: return 'HOLD'
        
    else: print('Invalid decide choice number')

def futurePercentChanges(similarPatternIndex):

    historicData = settings.historicData
    futureDistance = settings.futureDistance
    patternLength = settings.patternLength
    reqAverageChange = settings.reqAverageChange
    
    futurePercentageChanges = []
    for i in similarPatternIndex:
        currentPrice = historicData[i[0] + patternLength]
        futurePrice = historicData[i[0] + futureDistance + patternLength]
        percentage = percentageChange(currentPrice, futurePrice)
        futurePercentageChanges.append(percentage)

    return futurePercentageChanges
    
def decideLive(similarPatternIndexLive):

    decideMethodNumber = settings.decideMethodNumber
    reqNoSimilar = settings.reqNoSimilar
    reqAverageChange = settings.reqAverageChange
    
    if decideMethodNumber == 1:
        if len(similarPatternIndexLive) > reqNoSimilar:
            futurePercentageChanges = futurePercentChanges(similarPatternIndexLive)
            futurePercentageChanges.sort()
            #print(str(futurePercentageChanges))

            averageFuturePercentageChange = reduce(lambda x, y: x + y, futurePercentageChanges) / len(futurePercentageChanges)
            print(averageFuturePercentageChange)
            if averageFuturePercentageChange > reqAverageChange:
                return 'BUY'
            elif averageFuturePercentageChange < -reqAverageChange:
                return 'SELL'
            else:
                return'HOLD'
        else: return 'HOLD'
        
    else: print('Invalid decide choice number')
