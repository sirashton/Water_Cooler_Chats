import settings
#from settings import globalSettings
import csv
import matplotlib
import time
from shapeComparison import comparePattern
from shapeComparison import percentageChange
from dataProcessing import makeHistoricData
from matplotlib import pyplot
from functools import reduce
from graphingAndGUI import graphEverythingBacktesting
from findSimilar import findSimilar
from findSimilar import findSimilarLive
from decision import decide
from decision import decideLive
from profitLoss import profitLoss
from backtester import backtester
from backtester import liveTester



startTime = time.time()

settings.init('settings/1.1.txt')

#pastPatterns = []
#currentPatternIndex = -1000
#length = 15
#currentPattern = settings.historicData[currentPatternIndex : currentPatternIndex + length]
#print('Current Pattern : ' + str(currentPattern))
#historicData = historicData

'''def generatePastPatterns(patternLength, historicData):
    currentPoint = 0
    endPoint = len(historicData) - patternLength - futureDistance
    pastPatterns = []
    while currentPoint < endPoint:
        #print('Current Point ' +str(currentPoint))
        x = 0
        patternToAdd = []
        while x < patternLength + futureDistance:
            patternToAdd.append(historicData[currentPoint + x])
            #print('Data item to add' + str(historicData[currentPoint + x]))
            x += 1
            #print('x = ' + str(x))
        pastPatterns.append([patternToAdd,currentPoint])
        #print('Pattern to Add :' + str(patternToAdd))
        currentPoint += 1
    return pastPatterns'''

'''def graphSimilar():
    xList = []
    count = 0
    normalisedFuture = []
    for i in similarPatterns:
        normalised = []
        
        ratio = float(currentPattern[-1] / i[0][-(1 + futureDistance)])
        normalisedFuture.append(futurePrices[count] * ratio)
        if (futurePrices[count] * ratio) > currentPattern[-1]:
            pyplot.plot(25, futurePrices[count] * ratio , color = 'green')
        else:
            pyplot.plot(25, futurePrices[count] * ratio , color = 'red')
        #print(normalisedFuture)
        xList.append(25)
        for x in range(len(currentPattern) + futureDistance):
            normalised.append(i[0][x] * ratio)
        pyplot.plot(normalised)
        count += 1
    pyplot.plot(currentPattern,linewidth = 5.0)
    ''''''for x in range(len(currentPattern)):
            normalisedFuture.append(futurePrices[x] * ratio)
            xList.append(17)''''''
    #yList = futureResults(similarPatterns)
    yList = normalisedFuture
    print(yList)
    print(int(len(yList)))
    print(xList)
    print(int(len(xList)))
    #pyplot.scatter(xList, yList)
    pyplot.scatter(25,(historicData[startPosition + length + futureDistance])*ratio,color = 'blue')
    pyplot.show()'''

'''pastPatterns = generatePastPatterns(len(currentPattern), historicData)
similarPatterns = []
from shapeComparison import comparePattern
for i in pastPatterns:
    #print('Past pattern : '+str(i))
    if comparePattern(currentPattern,i[0],1) > 35:
        similarPatterns.append(i)'''


#currentPatternIndex = settings.currentPatternIndex

backtester()
'''pattern = [0.72724, 0.72790, 0.72991, 0.73194, 0.73058, 0.73333, 0.73373, 0.73222, 0.73185, 0.73152, 0.73152, 0.73230, 0.73427, 0.73477, 0.73609, 0.73480, 0.73600, 0.73515, 0.73528, 0.73493, 0.73236, 0.73604, 0.73527, 0.73986, 0.73231, 0.73082, 0.73110, 0.73083, 0.73007, 0.73291, 0.73336, 0.73027, 0.73023, 0.73040]
pattern = pattern[0:10]
pattern.reverse()
print(len(pattern))'''

#liveTester(pattern)

endtime = time.time()
print(endtime - startTime)
