def makeHistoricData():
    import csv
    data = []
    with open('EUR-GBP-1Hour-PreProcessed.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(float(row[2]))
    return data
