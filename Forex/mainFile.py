import csv
import matplotlib
from shapeComparison import comparePattern
from shapeComparison import percentageChange
from dataProcessing import makeHistoricData
from matplotlib import pyplot
from functools import reduce
from graphingAndGUI import graphEverythingBacktesting
from findSimilar import findSimilar
import settings

settings.init()


historicData = makeHistoricData()
#pastPatterns = []
currentPatternIndex = -1000
length = 15
currentPattern = historicData[currentPatternIndex : currentPatternIndex + length]
print('Current Pattern : ' + str(currentPattern))
historicData = historicData
futureDistance = 10

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

#futurePrices = []
'''def futureResults(similarPatterns):
    futureResults = []
    fururePrices = []
    for i in similarPatterns:
        futurePrice = historicData[i[1] + len(currentPattern) + futureDistance]
        futurePrices.append(futurePrice)
        futurePercentage = percentageChange(historicData[i[1] + len(currentPattern)],futurePrice)
        futureResults.append(futurePercentage)
    return futureResults
print('Found ' +str(len(similarPatterns)) + ' similar patterns')

print('Done')

print(futureResults(similarPatterns))
print(reduce(lambda x, y: x + y, futureResults(similarPatterns)) / float(len(futureResults(similarPatterns))))
graphSimilar()'''

similarPatternsIndex = findSimilar(currentPattern, historicData, futureDistance, 50, 1)
graphEverythingBacktesting(length, currentPatternIndex, similarPatternsIndex, historicData)
