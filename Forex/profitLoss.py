from shapeComparison import percentageChange
import settings

def profitLoss(decision, startIndex, endIndex):
    historicData = settings.historicData
    startPrice = historicData[startIndex]
    endPrice = historicData[endIndex]

    percentChange = percentageChange(startPrice, endPrice)

    if decision == 'HOLD':
        return 0
    if decision == 'BUY':
        return percentChange
    if decision == 'SELL':
        return -percentChange
