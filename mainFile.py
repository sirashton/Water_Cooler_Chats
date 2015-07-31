import csv
import matplotlib
from shapeComparison import comparePattern
from dataProcessing import makeHistoricData

currentPattern = []
historicData = makeHistoricData()

def generatePastPatterns(patternLength, historicData):
    currentPoint = 0
    endPoint = len(historicData) - patternLength
    pastPatterns = []
    while currentPoint < endPoint:
        x = 0
        patternToAdd = []
        while x < patternLength:
            patternToAdd.append(historicData[currentPoint + x])
            x += 1
        pastPatterns.append([patternToAdd,currentPoint])
    return pastPatterns


pastPatterns = generatePastPatterns(len(currentPattern), historicData)
similarPatterns = []
from shapeComparison import comparePattern
for i in pastPatterns:
    x = x
