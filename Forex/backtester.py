import settings
from findSimilar import findSimilar
from decision import decide
from profitLoss import profitLoss
from graphingAndGUI import graphEverythingBacktesting
from functools import reduce

def backtester():
    currentPatternIndex = 1
    patternLength = settings.patternLength
    futureDistance = settings.futureDistance
    allProfits = []
    noTrades = 0
    noTrys = 0
    for i in range(0,100000):
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
