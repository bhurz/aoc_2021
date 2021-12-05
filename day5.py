import collections
import re

MAPSIZE = 1000

def ParseFile( filePath ):
    print( '* Loading\t%s' % filePath )
    coordinateList = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        lines = fileHandle.readlines()
        for lineNum, line in enumerate(lines):
            coordinatePair = line.strip().split("->")
            firstCoordinate = [ int(coordinate) for coordinate in coordinatePair[0].strip().split(",") ]
            secondCoordinate = [ int(coordinate) for coordinate in coordinatePair[1].strip().split(",") ]
            coordinatePair = []
            coordinatePair.extend(firstCoordinate)
            coordinatePair.extend(secondCoordinate)
            coordinateList.append(coordinatePair)
    return coordinateList

def CountOverlappingPoints( coordinatesList, considerDiagonal = False ):
    coordinateMap = [[0]*MAPSIZE for i in range(MAPSIZE)]
    
    for point1X,point1Y, point2X,point2Y in coordinatesList:
        if considerDiagonal:
            if point1X > point2X:
                point2X, point1X = point1X, point2X
                point2Y, point1Y = point1Y, point2Y
            
            if point2X > point1X:
                if point2Y > point1Y:
                    for i in range(point2Y-point1Y+1):
                        coordinateMap[point1Y+i][point1X+i]+=1
                elif point2Y < point1Y:
                    for i in range(point1Y-point2Y+1):
                        coordinateMap[point1Y-i][point1X+i]+=1
                else:
                    for i in range(point1X, point2X+1):
                        coordinateMap[point1Y][i]+=1
            else:
                first,second = min(point1Y, point2Y), max(point1Y, point2Y)
                for i in range(first, second+1):
                    coordinateMap[i][point1X]+=1
        else:
            if point1X == point2X:
                first,second = min(point1Y, point2Y), max(point1Y, point2Y)
                for i in range(first, second+1):
                    coordinateMap[i][point1X]+=1
            elif point1Y == point2Y:
                first,second = min(point1X, point2X), max(point1X, point2X)
                for i in range(first, second+1):
                    coordinateMap[point1Y][i]+=1

    count = 0
    for i in range(MAPSIZE):
        for j in range(MAPSIZE):
            if coordinateMap[i][j] >=2:
                count += 1

    return count 

if __name__ == '__main__':
    coordinateList = ParseFile( "D:\\Github\\aoc_2021\\day5_sample.csv" )
   
    ans = CountOverlappingPoints(coordinateList, False )
    print("Output 1:{}".format(ans))
    
    ans = CountOverlappingPoints(coordinateList, True )
    print("Output 2:{}".format(ans))
