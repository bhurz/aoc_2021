import collections
import re

MAPSIZE = 1000

def ParseFile( filePath ):
    print( '* Loading\t%s' % filePath )
    positions = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        lines = fileHandle.readlines()
        for line in lines:
            positions = [ int(val )for val in line.split(",") ]
    
    return positions

def FuleSpent( positions ):
    positionsCounter = collections.Counter(positions)
    minPosition = min( positionsCounter.keys() )
    maxPosition = max( positionsCounter.keys() )
    
    minFuelSpent = float('inf')
    minFuelPosition = 0

    for p in range(minPosition, maxPosition + 1 ):
        fuelSpent = 0
        for k,v in positionsCounter.items():
            positionDelta = abs(p-k)
            fuelSpent += (positionDelta*v)
        
        if fuelSpent < minFuelSpent:
            minFuelSpent = fuelSpent
            minFuelPosition = p

    return minFuelSpent

def FuleSpentExp( positions ):
    positionsCounter = collections.Counter(positions)
    minPosition = min( positionsCounter.keys() )
    maxPosition = max( positionsCounter.keys() )
    
    minFuelSpent = float('inf')
    minFuelPosition = 0

    for p in range(minPosition, maxPosition + 1 ):
        fuelSpent = 0
        for k,v in positionsCounter.items():
            positionDelta = abs(p-k)
            fuelSpent += (positionDelta*(positionDelta+1)*v)//2
        if fuelSpent < minFuelSpent:
            minFuelSpent = fuelSpent
            minFuelPosition = p

    return minFuelSpent

if __name__ == '__main__':
    positions = ParseFile( "D:\\Github\\aoc_2021\\day7_sample.csv" )
   
    ans = FuleSpent(positions )
    print("Output 1:{}".format(ans))

    ans = FuleSpentExp(positions )
    print("Output 1:{}".format(ans))