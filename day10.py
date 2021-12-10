import collections
import re
import sys

class Solution:
    OPEN_BRACKETS = {"(", "<", "{", "[" }
    CLOSE_BRACKETS = {")", ">", "}", "]" }
    BRACKETS_PAIR_INVERTED = { ")":"(", ">":"<", "}":"{", "]":"["}
    BRACKETS_PAIR = { "(":")", "<":">", "{":"}", "[":"]"}

    BRACKET_SCORE_MAPPING = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    BRACKET_COMPLETION_SCORE_MAPPING = { ")": 1, "]": 2, "}": 3, ">": 4 }

    def __init__( self, filePath ):
        self.input = []
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                self.input.append(list(line.strip()))
    
    def _computeScore(self, bracketList ):
        score = 0
        for bracket in bracketList:
            score+= Solution.BRACKET_SCORE_MAPPING[bracket]
        
        return score
    
    def _computeCompletionScore(self, completionList ):
        scoreList = []
        for bracketList in completionList:
            score = 0
            for bracket in bracketList:
                score = score * 5 + Solution.BRACKET_COMPLETION_SCORE_MAPPING[bracket]
            scoreList.append( score )
        scoreList.sort()
        middleElementIndex = len(scoreList)//2
        return scoreList[middleElementIndex]

    def SolvePart1(self):
        corruptLineBrackets = []
        for row in self.input:
            stack = []
            for bracket in row:
                #Push open brackets onto the stack
                if bracket in Solution.OPEN_BRACKETS:
                    stack.append( bracket)
                elif bracket in Solution.CLOSE_BRACKETS:
                    top = stack[-1]
                    stack.pop()
                    if Solution.BRACKETS_PAIR_INVERTED[bracket] != top:
                        corruptLineBrackets.append(bracket)
                        break
        score = self._computeScore( corruptLineBrackets )
        print("Output 1: {}".format(score))

    def SolvePart2(self):
        completionBracketList= []
        for row in self.input:
            stack = []
            corruptedLine = False
            for bracket in row:
                #Push open brackets onto the stack
                if bracket in Solution.OPEN_BRACKETS:
                    stack.append( bracket)
                elif bracket in Solution.CLOSE_BRACKETS:
                    top = stack[-1]
                    stack.pop()
                    if Solution.BRACKETS_PAIR_INVERTED[bracket] != top:
                        corruptedLine = True
                        break
            if not corruptedLine and len(stack) > 0:
                toggleBrackets = []
                for bracket in stack:
                    toggleBrackets.append( Solution.BRACKETS_PAIR[bracket] )
                
                toggleBrackets.reverse()
                completionBracketList.append(toggleBrackets)


        score = self._computeCompletionScore( completionBracketList )
        print("Output 2: {}".format(score))

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day10_input.txt" )
    obj.SolvePart1()
    obj.SolvePart2()

