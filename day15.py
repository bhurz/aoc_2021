import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.S = []
        self.R = {}
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for lineNum, line in enumerate(lines):
                if line == "\n":
                    continue
                elif lineNum == 0:
                    self.S = line.strip()
            
                else:
                    start, end = line.strip().split(" -> ")
                    self.R[start] = end

    def SolvePart1( self, steps ):
         
        C1 = collections.Counter()
        for i in range(len(self.S)-1):
            C1[self.S[i:i+2]] += 1

        for t in range(41):
            if t in [10,40]:
                CF = collections.Counter()
                for k in C1:
                    CF[k[0]] += C1[k]
                CF[self.S[-1]] += 1
                print(max(CF.values())-min(CF.values()))

            C2 = collections.Counter()
            for k in C1:
                C2[k[0]+self.R[k]] += C1[k]
                C2[self.R[k]+k[1]] += C1[k]
            C1 = C2
if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day14_input.txt" )
    obj.SolvePart1(40)