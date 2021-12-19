import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.exp = []
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                temp= []
                for c in line:
                    if c != ',':
                        if c.isdigit():
                            temp.append(int(c))
                        else:
                            temp.append(c)
                    
                self.exp.append( temp )

    def addExp( self, prev, curr ):
        exp = []
        exp.append('[')
        exp.extend(prev)
        exp.extend(curr)
        exp.extend(']')

        explode = True
        split = False

        while explode or split:
            obc = 0
            temp = []
            f = True
            for c in exp:
                if obc >= 4 and f:
                    temp.append(c)
                    if c == '[':
                        obc += 1
                    elif c == ']':
                        obc -= 1
                        if obc <= 3:
                            f = False
                else:
                    if c == '[':
                        obc += 1
                    elif c == ']':
                        obc -= 1
            print(temp)


    def SolvePart1( self ):
        prevExp = self.exp[0]
        for i in range( 1, len(self.exp) ):
            currExp = self.exp[i]
            prevExp = self.addExp(prevExp, currExp )

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day18_input.txt" )
    ans = obj.SolvePart1()

    print(ans)