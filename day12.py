import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.nodeMap = {}
        self.caveSize = {}
        self.edges = []

        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            currNodeNum = 0
            for line in lines:
                nodes = line.strip().split("-")
                if nodes[0] not in self.nodeMap:
                    self.nodeMap[nodes[0]] = ( currNodeNum )
                    self.caveSize[currNodeNum] = nodes[0].isupper()
                    currNodeNum+=1

                if nodes[1] not in self.nodeMap:
                    self.nodeMap[nodes[1]] = ( currNodeNum )
                    self.caveSize[currNodeNum] = nodes[1].isupper()
                    currNodeNum+=1
                
                self.edges.append( ( self.nodeMap[nodes[0]], self.nodeMap[nodes[1]] ))
                self.edges.append( ( self.nodeMap[nodes[1]], self.nodeMap[nodes[0]] ))

        nodeCount = len(self.nodeMap)
        self.graph = [[0]*nodeCount for _ in range(nodeCount) ]
        for u, v in self.edges:            
            self.graph[u][v] = 1

    def isAnySmallCaveVisitedTwice(self):
        for key in self.caveSize:
            if not self.caveSize[key]:
                if self.pathNodes[key] == 2:
                    return True
        return False

    def dfsPart2( self, node ):
        
        if self.nodeMap['end'] == node:
            self.pathCount += 1
            self.pathNodes[node] -= 1
            return

        for neighbor in range(len(self.graph[0])):
            if self.graph[node][neighbor] == 1:
                if ( neighbor == self.nodeMap['end'] or neighbor == self.nodeMap['start'] ) and self.pathNodes[neighbor] == 1:
                    continue
                if not self.caveSize[neighbor] and self.isAnySmallCaveVisitedTwice() and ( self.pathNodes[neighbor] == 2 or self.pathNodes[neighbor] == 1) :
                    continue
                else:
                    self.pathNodes[neighbor]+=1
                    self.dfsPart2(neighbor)
        
        self.pathNodes[node] -= 1

    def dfsPart1( self, node ):
        
        if self.nodeMap['end'] == node:
            self.pathCount += 1
            self.pathNodes[node] -= 1
            return

        for neighbor in range(len(self.graph[0])):
            if self.graph[node][neighbor] == 1:
                if ( neighbor == self.nodeMap['end'] or neighbor == self.nodeMap['start'] ) and self.pathNodes[neighbor] == 1:
                    continue
                if not self.caveSize[neighbor] and self.pathNodes[neighbor] == 1:
                    continue
                else:
                    self.pathNodes[neighbor]+=1
                    self.dfsPart1(neighbor)
        
        self.pathNodes[node] -= 1

    def SolvePart1( self ):
        self.pathNodes = collections.defaultdict(int)
        self.pathCount = 0
        startNode = self.nodeMap['start']
        self.pathNodes[ startNode ] += 1
        self.dfsPart1(startNode)
        print("Output 1 : {}".format(self.pathCount))

    def SolvePart2( self ):
        self.pathNodes = collections.defaultdict(int)
        self.pathCount = 0
        startNode = self.nodeMap['start']
        self.pathNodes[ startNode ] += 1
        self.dfsPart2(startNode)
        print("Output 1 : {}".format(self.pathCount))

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day12_input.txt" )
    obj.SolvePart1()
    obj.SolvePart2()