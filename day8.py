import collections
import re
import sys

MAPSIZE = 1000

def ParseFile( filePath ):
    print( '* Loading\t%s' % filePath )
    input = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        lines = fileHandle.readlines()
        for line in lines:
            signals, output =  tuple( line.strip().split("|") )
            input.append( [ signals.strip().split(" "), output.strip().split(" ") ] )
    return input

def CountDigitsAlt(entries):
    total = 0
    for entry in entries:  
        for pattern in entry[0] + entry[1]:
            if len(pattern) == 2: one = set(pattern)
            if len(pattern) == 4: four = set(pattern)
        
        number = ""
        for pattern in entry[1]:
            if len(pattern) == 2: number += "1"
            elif len(pattern) == 3: number += "7"
            elif len(pattern) == 4: number += "4"
            elif len(pattern) == 7: number += "8"
            elif len(pattern) == 5:
                if len(one.intersection(pattern)) == 2: number += "3"
                elif len(four.intersection(pattern)) == 3: number += "5"
                else: number += "2"
            elif len(pattern) == 6:
                if len(four.intersection(pattern)) == 4: number += "9"
                elif len(one.intersection(pattern)) == 2: number += "0"
                else: number += "6"
        total += int(number)
    print(total)

if __name__ == '__main__':
    input = ParseFile( "D:\\Github\\aoc_2021\\day8_sample.csv" )

    ans = CountDigitsAlt(input)
