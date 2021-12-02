import csv
direction = {"forward": 1, "up": 2, "down": 3}

def ParseCsv( filePath ):
    print( '* Loading\t%s' % filePath )
    fileData = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        reader = csv.reader( fileHandle )
        for row in reader:
            commandKVP = row[0].split(' ')
            fileData.append((direction[commandKVP[0]], int(commandKVP[1])))

    return fileData

def GetFinalSubmarinePosition( fileData ):
    horizontal, depth = 0, 0
    for command, distance in fileData:
        if command == 1:
            horizontal += distance
        elif command == 2:
            depth -= distance
        else:
            depth += distance

    return horizontal, depth

def GetFinalSubmarinePositionWithAim( fileData ):
    horizontal, depth, aim = 0, 0, 0
    for command, distance in fileData:
        if command == 1:
            horizontal += distance
            depth += (aim*distance)
        elif command == 2:
            aim -= distance
        else:
            aim += distance

    return horizontal, depth

if __name__ == '__main__':
    fileData = ParseCsv( "D:\\Github\\aoc_2021\\day2_sample.csv" )
    horizontal, depth = GetFinalSubmarinePosition(fileData)
    print( "Output 1: {}*{} --> {}".format(horizontal, depth, horizontal*depth) )

    horizontal, depth = GetFinalSubmarinePositionWithAim(fileData)
    print( "Output 2: {}*{} --> {}".format(horizontal, depth, horizontal*depth) )
