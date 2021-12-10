import collections
import re
import sys

class Solution:
    def __init__( self, filePath ):
        self.input = []
        self.directions = [(0,1),(0, -1), (1, 0), (-1, 0)]
        self.visited = set()
        with open( filePath, 'r', newline='' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                self.input.append(list( map( int, list(line.strip()))) )
    
    def _dfs(self, row, col ):
        maxCols = len(self.input[0])
        maxRows = len(self.input)
        self.visited.add( (row, col ) )
        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row >= 0 and new_row < maxRows and new_col >= 0 and new_col < maxCols and self.input[new_row][new_col] != 9 and (new_row, new_col ) not in self.visited:
                self._dfs( new_row, new_col )

    def SolvePart1(self):
        totalHeight = 0
        maxCols = len(self.input[0])
        maxRows = len(self.input)

        for row in range(maxRows):
            for col in range(maxCols):
                height = self.input[row][col]
                lowPoint = True
                for direction in self.directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row >= 0 and new_row < maxRows and new_col >= 0 and new_col < maxCols and self.input[new_row][new_col] <= height:
                        lowPoint = False
                        break
                if lowPoint:
                    totalHeight += ( height + 1 )
        
        print("Output 1: {}".format(totalHeight))

    def SolvePart2(self):
        maxCols = len(self.input[0])
        maxRows = len(self.input)

        basinSizeList = []
        for row in range(maxRows):
            for col in range(maxCols):
                height = self.input[row][col]
                lowPoint = True
                for direction in self.directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row >= 0 and new_row < maxRows and new_col >= 0 and new_col < maxCols and self.input[new_row][new_col] <= height:
                        lowPoint = False
                        break
                if lowPoint:
                    self.visited = set()
                    self._dfs( row, col )
                    basinSizeList.append(len(self.visited))
        
        basinSizeList.sort( reverse = True )
        ans = basinSizeList[0]*basinSizeList[1]*basinSizeList[2]
        print("Output 2: {}".format(ans))

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day9_sample.csv" )
    obj.SolvePart1()
    obj.SolvePart2()

