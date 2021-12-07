import collections
import re

MAPSIZE = 1000

def ParseFile( filePath ):
    print( '* Loading\t%s' % filePath )
    age = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        lines = fileHandle.readlines()
        for line in lines:
            age = [ int(val )for val in line.split(",") ]
    
    return age

def LanternFishCountOptimized( input, days ):
    ageCounter = collections.defaultdict(int)
    initialAgeCounter = collections.Counter(input)
    for k,v in initialAgeCounter.items():
        ageCounter[k] = v

    for _ in range(days):
        prev = 0
        curr = 0
        for i in range(8, -1, -1 ):
            curr = ageCounter[i]
            ageCounter[i] = prev
            prev = curr

        if curr > 0:
            ageCounter[6] += curr
            ageCounter[8] += curr

    return sum(ageCounter.values())

if __name__ == '__main__':
    ageList = ParseFile( "D:\\Github\\aoc_2021\\day6_sample.csv" )
   
    ans = LanternFishCountOptimized(ageList, 80 )
    print("Output 1:{}".format(ans))

    ans = LanternFishCountOptimized(ageList, 256 )
    print("Output 2:{}".format(ans))
