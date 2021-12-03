import csv
import collections

def ParseCsv( filePath ):
    print( '* Loading\t%s' % filePath )
    fileData = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        reader = csv.reader( fileHandle )
        for row in reader:
            bitsList = list(row[0])
            fileData.append(bitsList)

    return fileData

def GetPowerConsumption( fileData ):
    gammaList = []
    epsilonList = []

    for index in range( len( fileData[0])):
        count = collections.Counter( [ item[index] for item in fileData] )
        sortedCountList = count.most_common()
        gammaList.append(sortedCountList[0][0])
        epsilonList.append(sortedCountList[1][0])
    
    gammaRate = int( "".join(str(x) for x in gammaList ), 2)
    epsilonRate = int( "".join(str(x) for x in epsilonList ), 2)
    return gammaRate*epsilonRate

def GetOxygenRating( fileData ):
    
    temp = fileData[:]
    index = 0
    solutionLen = len(temp)

    while solutionLen > 1:
        count1s = 0
        result = []
        for item in temp:
            if item[index] == '1':
                count1s += 1
            else:
                count1s -= 1
        
        # Keep entries with 1
        if count1s >= 0:      
            for i, item in enumerate(temp):
                if item[index] == '1':
                    result.append(item)
        else:
            for i, item in enumerate(temp):
                if item[index] == '0':
                    result.append(item)
        temp = result[:]
        solutionLen = len(temp)
        index += 1

    oxygenRating = int( "".join(x for x in temp[0] ), 2)
    return oxygenRating

def GetCORating( fileData ):
    
    temp = fileData[:]
    index = 0
    solutionLen = len(temp)

    while solutionLen > 1:
        count1s = 0
        result = []
        for item in temp:
            if item[index] == '1':
                count1s += 1
            else:
                count1s -= 1
        
        # Keep entries with 1
        if count1s >= 0:      
            for i, item in enumerate(temp):
                if item[index] == '0':
                    result.append(item)
        else:
            for i, item in enumerate(temp):
                if item[index] == '1':
                    result.append(item)
        temp = result[:]
        solutionLen = len(temp)
        index += 1

    coRating = int( "".join(x for x in temp[0] ), 2)
    return coRating

if __name__ == '__main__':
    fileData = ParseCsv( "D:\\Github\\aoc_2021\\day3_sample.csv" )
    powerConsumption = GetPowerConsumption(fileData)
    print("Output 1 {}".format(powerConsumption))

    lsRating = GetOxygenRating( fileData )
    coRating = GetCORating( fileData )
    print("Output 2 {}".format(lsRating*coRating))