import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                l = line.strip().split(": ")[1].split(", ")
                xRange = l[0].split("=")[1].split("..")
                self.xMin = int(xRange[0])
                self.xMax = int(xRange[1])
                yRange = l[1].split("=")[1].split("..")
                self.yMin = int( yRange[0] )
                self.yMax = int(yRange[1])


    def UpdateCoordinateAndVelocity(self, x, y, xv, yv ):
        x += xv
        y += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1

        yv -= 1
        return x, y, xv, yv

    def SolvePart1( self ):
        absoluteYMax = 0
        initialVelocity = set()
        for xVel in range(1, 117):
            for yVel in range(-198, 400):
                x, y = 0, 0
                xv, yv = xVel, yVel
                ym = 0

                while True:
                    x, y, xv, yv = self.UpdateCoordinateAndVelocity( x, y, xv, yv )
                    if y > ym:
                        ym = y

                    if y < self.yMin or x > self.xMax:
                        break
                    if y <= self.yMax and y >= self.yMin and x >= self.xMin and x <= self.xMax:
                        initialVelocity.add((xVel,yVel))
                        if ym > absoluteYMax:
                            absoluteYMax = ym
                        break
        print(initialVelocity)
        print(len(initialVelocity))
        temp1 = max( list( map( lambda x: x[0], initialVelocity ) ) )
        temp2 = min( list( map( lambda x: x[0], initialVelocity ) ) )
        temp3 = max( list( map( lambda x: x[1], initialVelocity ) ) )
        temp4 = min( list( map( lambda x: x[1], initialVelocity ) ) )

        print(temp1, temp2, temp3, temp4 )
        return absoluteYMax




if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day17_input.txt" )
    ans = obj.SolvePart1()

    print(ans)