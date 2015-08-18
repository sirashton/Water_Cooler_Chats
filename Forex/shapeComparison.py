from functools import reduce

def percentageChange(dataFrom, dataTo):#Calculates exactly what you'd think
    if dataFrom == 0:
        return 0
    return ((float(dataTo) - float(dataFrom))/abs(float(dataFrom)))*100.0

def percentageSteps(data):                                              #creates a list of percentage changes between each step in the data,
                                                                        #list generated will be shorter by 1 that original data
    output = []
    for i in range(len(data)-1):
        output.append(percentageChange(data[i],data[i+1]))
    return output

def logarithmicChange(dataFrom,dataTo):
    x=x

def comparePattern(pattern1,pattern2,methodNumber):
    if methodNumber == 1.0:                                             #percentage change comparison
        pattern1Steps = percentageSteps(pattern1)                       #Change to data to percentage steps
        #print('Pattern 1 Steps ' + str(pattern1Steps))
        pattern2Steps = percentageSteps(pattern2)
        #print('Pattern 2 steps ' + str(pattern2Steps))
        differencesInChanges = []
        for i in range(len(pattern1Steps)):
            #print(100- abs(percentageChange(pattern1Steps[i],pattern2Steps[i])))
            differencesInChanges.append(100- abs(percentageChange(pattern1Steps[i],pattern2Steps[i])))
        #print(differencesInChanges)
        averageDifference = reduce(lambda x, y: x + y, differencesInChanges) / float(len(differencesInChanges))
        return averageDifference
