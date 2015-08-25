import settings
from findSimilar import findSimilar
from findSimilar import findSimilarLive
from decision import decide
from decision import decideLive
from profitLoss import profitLoss
from graphingAndGUI import graphEverythingBacktesting
from graphingAndGUI import graphEverythingLive
from functools import reduce

def backtester():
    currentPatternIndex = 1
    patternLength = settings.patternLength
    futureDistance = settings.futureDistance
    allProfits = []
    noTrades = 0
    noTrys = 0
    for i in range(0,1000):
        similarPatternsIndex = findSimilar(currentPatternIndex)
        decision = decide(similarPatternsIndex)
        print(decision)
        noTrys += 1
        print('Attempt number : ' + str(noTrys))
        if decision != 'HOLD':
            profit = profitLoss(decision, currentPatternIndex + patternLength, currentPatternIndex + patternLength + futureDistance)
            print('Profit from this trade : ' + str(profit))
            allProfits.append(profit)
            averageProfit = reduce(lambda x, y: x + y, allProfits) / len(allProfits)
            print('Average profit         : ' + str(averageProfit))
            totalProfit = sum(allProfits)
            print('Total profit           : ' + str(totalProfit))
            noTrades += 1
            print('Number of trades       : ' + str(noTrades))
            #graphEverythingBacktesting(similarPatternsIndex, currentPatternIndex)
        currentPatternIndex += 10
        #print(currentPatternIndex)
        #createCurrentPattern()
    hourlyProfit = ((averageProfit - 0.015)*25000*noTrades) / (noTrys*10)
    print('HOURLY PROFIT = ' + str(hourlyProfit))
    return hourlyProfit

def liveTester(pattern):
    
    patternLength = settings.patternLength
    futureDistance = settings.futureDistance
    allProfits = []
    similarPatternsIndexLive = findSimilarLive(pattern)
    decision = decideLive(similarPatternsIndexLive)
    print(decision)
    if decision != 'HOLD':

        '''print('Profit from this trade : ' + str(profit))
        allProfits.append(profit)
        averageProfit = reduce(lambda x, y: x + y, allProfits) / len(allProfits)
        print('Average profit         : ' + str(averageProfit))
        totalProfit = sum(allProfits)
        print('Total profit           : ' + str(totalProfit))
        noTrades += 1
        print('Number of trades       : ' + str(noTrades))'''
    graphEverythingLive(similarPatternsIndexLive, pattern)


    
