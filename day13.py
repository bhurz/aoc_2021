import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.dotsCoord = set()
        self.lineBreak = []
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                if line == "\n":
                    continue
                elif line[0:4] == 'fold':
                    fold = line.strip().split("=")
                    if fold[0][-1] == "x":
                        self.lineBreak.append(("x", int(fold[1])))
                    else:
                        self.lineBreak.append(("y", int(fold[1])))
                else:
                    coordinates = line.strip().split(",")
                    self.dotsCoord.add( ( int(coordinates[0]), int(coordinates[1]) ) )

    def SolvePart1( self ):
        
        for axis, foldVal in self.lineBreak:
            coords = set()
            if axis == "y":
                for coordinate in self.dotsCoord:
                    x = coordinate[0]
                    y = coordinate[1]
                    if y > foldVal:
                        y_new = foldVal - (y - foldVal)
                        coords.add( ( x, y_new ) )
                    else:
                        coords.add( ( x, y ) )
                self.dotsCoord = coords
            else:
                for coordinate in self.dotsCoord:
                    x = coordinate[0]
                    y = coordinate[1]
                    if x > foldVal:
                        x_new = foldVal - (x - foldVal)
                        coords.add( ( x_new, y ) )
                    else:
                        coords.add( ( x, y ) )
                self.dotsCoord = coords

        matrix = [[0]*40 for _ in range(6)]
        for i in range(6):
            for j in range(40):
                if (j,i) in self.dotsCoord:
                    matrix[i][j] = 1
        
        for i in range(6):
            print(matrix[i])

        print("Output for Part 1: {}".format( len(self.dotsCoord)))
if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day13_input.txt" )
    obj.SolvePart1()