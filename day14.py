import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.graph = []

        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                self.graph.append( list( map( int, list(line.strip())) ) )

    def FindMinumumWeightNode(self):
        minWeight = sys.maxsize
        minu = 0
        minv = 0
        for key in self.D:
            u , v = key
            val = self.D[(u,v)]
            if val < minWeight and (u,v) not in self.dst:
                minWeight = val
                minu = u
                minv = v
        return minWeight, minu, minv

    def SolvePart1( self ):
        vertices = len( self.graph )
        self.dst = set()
        self.D = {}
        self.D[ ( 0, 0 ) ] = 0
        
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        while len(self.dst) < vertices*vertices:
            w, u, v = self.FindMinumumWeightNode()
            self.dst.add( (u, v ) )
            for direction in directions:
                new_u = u + direction[0]
                new_v = v + direction[1]
                if new_u >= 0 and new_u < vertices and new_v >=0 and new_v < vertices:
                    new_w = w + self.graph[new_u][new_v]
                    if (new_u, new_v) not in self.D:
                        self.D[( new_u, new_v )] = new_w
                    elif (new_u, new_v) in self.D and new_w < self.D[( new_u, new_v )]:
                        self.D[( new_u, new_v )] = new_w

        return self.D[( vertices -1, vertices-1 )]

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day14_input.txt" )
    ans = obj.SolvePart1()
    print(ans)