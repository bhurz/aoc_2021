import collections
import re
import sys
from collections import deque
import heapq

class Solution:
    def __init__( self, filePath, nTiles ):
        g = []
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                g.append( list( map( int, list(line.strip())) ) )

        vertices = len(g)

        self.graph = [[0]*vertices*nTiles for _ in range(vertices*nTiles) ]
        for row in range(vertices*nTiles):
            row_increment = row//vertices
            base_row = row % vertices
            for col in range(vertices*nTiles):
                col_increment = col//vertices
                base_col = col%vertices
                val = g[base_row][base_col] + row_increment + col_increment
                
                if val >= 10:
                    val -= 9

                self.graph[row][col] = val

    def SolvePart1( self ):
        vertices = len( self.graph )
        self.heap = [(0,0,0)]
        self.D = {}
        self.D[ ( 0, 0 ) ] = 0
        self.visited = set()

        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        while len(self.visited) < vertices*vertices:
            w, u, v = heapq.heappop( self.heap )
            if (u, v ) == ( vertices -1, vertices-1 ):
                break

            if ( u, v ) not in self.visited:
                self.visited.add( (u, v ) )
            else:
                continue

            for direction in directions:
                new_u = u + direction[0]
                new_v = v + direction[1]
                if new_u >= 0 and new_u < vertices and new_v >=0 and new_v < vertices:
                    new_w = w + self.graph[new_u][new_v]
                    if (new_u, new_v) not in self.D:
                        self.D[( new_u, new_v )] = new_w
                        heapq.heappush( self.heap, (new_w, new_u, new_v ) )
                    elif (new_u, new_v) in self.D and new_w < self.D[( new_u, new_v )]:
                        self.D[( new_u, new_v )] = new_w
                        heapq.heappush( self.heap, (new_w, new_u, new_v ) )

        return self.D[( vertices -1, vertices-1 )]

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day14_input.txt", 5 )
    ans = obj.SolvePart1()
    print(ans)