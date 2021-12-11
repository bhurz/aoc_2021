import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        self.input = []
        self.directions = [(0,1),(0,-1),(1,0),(-1,0), (1,1),(1,-1),(-1,1),(-1,-1) ]
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                self.input.append(list( map(int, list(line.strip())) ))
    
    def SolvePart1(self, steps ):
        data = [ row[:] for row in self.input]
        maxRows = len(data)
        maxCols = len(data[0])
        
        totalFlashCount = 0
        for step in range(steps):
            flashCells = deque()
            flashCountPerStep = 0
            #increment in this phase and colled the cells which are about to flash because they are set at 9
            for row in range(maxRows):
                for col in range(maxCols):
                    if data[row][col] == 9:
                        flashCells.append( (row, col ) )
                        data[row][col] = 0
                        flashCountPerStep += 1
                    else:
                        data[row][col] += 1

            while flashCells:
                row, col = flashCells.popleft()
                for direction in self.directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row >=0 and new_row < maxRows and new_col >=0 and new_col < maxCols and data[new_row][new_col] != 0:
                        if data[new_row][new_col] == 9:
                            data[new_row][new_col] = 0
                            flashCountPerStep += 1
                            flashCells.append(( new_row, new_col ))
                        else:
                            data[new_row][new_col] += 1

            totalFlashCount += flashCountPerStep
        print("Output 1: {}".format(totalFlashCount))

    def SolvePart2(self):
        data = [ row[:] for row in self.input]
        maxRows = len(self.input)
        maxCols = len(self.input[0])
        
        totalFlashCount = 0
        step = 0
        while True:
            flashCells = deque()
            flashCountPerStep = 0
            #increment in this phase and colled the cells which are about to flash because they are set at 9
            for row in range(maxRows):
                for col in range(maxCols):
                    if data[row][col] == 9:
                        flashCells.append( (row, col ) )
                        data[row][col] = 0
                        flashCountPerStep += 1
                    else:
                        data[row][col] += 1

            while flashCells:
                row, col = flashCells.popleft()
                for direction in self.directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row >=0 and new_row < maxRows and new_col >=0 and new_col < maxCols and data[new_row][new_col] != 0:
                        if data[new_row][new_col] == 9:
                            data[new_row][new_col] = 0
                            flashCountPerStep += 1
                            flashCells.append(( new_row, new_col ))
                        else:
                            data[new_row][new_col] += 1

            totalFlashCount += flashCountPerStep
            step += 1
            if flashCountPerStep == 100:
                print("Output 2: {}".format(step))
                break

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day11_input.txt" )
    obj.SolvePart1( 100 )
    obj.SolvePart2()
