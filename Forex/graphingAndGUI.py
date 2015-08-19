import matplotlib
from matplotlib import pyplot

def graphEverythingBacktesting(patternLength, currentPatternIndex, similarPatternsIndex, historicData, futureDistance):

    currentPattern = historicData[currentPatternIndex : currentPatternIndex + patternLength + futureDistance]    #plot similar graphs (opacity based on closeScore?)

    #plot future prices (red green if above/below)

    for i in similarPatternsIndex:
        patternToPlot = historicData[ i[0] : i[0] + patternLength + futureDistance]
        ratio = (currentPattern[-1 - futureDistance])/(patternToPlot[-1 - futureDistance])
        
        pyplot.plot(normalise(patternToPlot, ratio), color = 'grey',alpha = 0.5)
        
        xCoord = patternLength + futureDistance

        if patternToPlot[-1] > patternToPlot[-1 - futureDistance]:
            pyplot.scatter(xCoord, patternToPlot[-1] * ratio, color = 'green', alpha = 0.5)
        if patternToPlot[-1] < patternToPlot[-1 - futureDistance]:
            pyplot.scatter(xCoord, patternToPlot[-1] * ratio, color = 'red', alpha = 0.5)
    #plotCurrent Graph
    pyplot.plot(currentPattern, color='black')
    pyplot.scatter(xCoord, currentPattern[-1],color = 'black')
    pyplot.show()

def normalise(data, ratio):
    output = []
    for i in range(len(data)):
        output.append(data[i] * ratio)
    return output
