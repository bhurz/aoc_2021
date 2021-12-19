import collections
import re
import sys
from collections import deque

class Solution:
    def __init__( self, filePath ):
        mapping = {
            "0" : "0000",
            "1" : "0001",
            "2" : "0010",
            "3" : "0011",
            "4" : "0100",
            "5" : "0101",
            "6" : "0110",
            "7" : "0111",
            "8" : "1000",
            "9" : "1001",
            "A" : "1010",
            "B" : "1011",
            "C" : "1100",
            "D" : "1101",
            "E" : "1110",
            "F" : "1111",
        }

        self.binaryStr = ""
        with open( filePath, 'r' ) as fileHandle:
            lines = fileHandle.readlines()
            for line in lines:
                for c in line:
                    self.binaryStr += mapping[c]
        
        self.versionSum = 0
        self.queue = []
        self.packetTypes = { 0: "SM", 1 : "PR", 2: "MN", 3: "MX", 5: "GR", 6: "LS", 7: "EQ" }
        
    def _pushInQueue( self, value, isType ):
        
        if isType == 1:
            self.queue.append( self.packetTypes[value] )
        else:
            self.queue.append( value )

    def _compute(self):
        val = []
        operation = None
        ans = 0
        while self.queue:
            poppedVal = self.queue.pop(0)
            if poppedVal in self.packetTypes.values() and operation:
                if operation == "SM":
                    ans += sum(val)
                elif operation == "PR":
                    temp = 1
                    for i in range(len(val)):
                        temp = temp*val[i]
                    ans += temp
                elif operation == "MN":
                    ans += min( val )
                elif operation == "MX":
                    ans += max(val )
                elif operation == "GR":
                    if val[0] > val[1]:
                        ans += 1
                elif operation == "LS":
                    if val[0] < val[1]:
                        ans += 1
                elif operation == "EQ":
                    if val[0] == val[1]:
                        ans += 1
                val = []

            if poppedVal in self.packetTypes.values():
                operation = poppedVal
            else:
                val.append(poppedVal)
        
        if operation == "SM":
            ans += sum(val)
        elif operation == "PR":
            temp = 1
            for i in range(len(val)):
                temp = temp*val[i]
            ans += temp
        elif operation == "MN":
            ans += min( val )
        elif operation == "MX":
            ans += max(val )
        elif operation == "GR":
            if val[0] > val[1]:
                ans += 1
        elif operation == "LS":
            if val[0] < val[1]:
                ans += 1
        elif operation == "EQ":
            if val[0] == val[1]:
                ans += 1

        return ans

    def ParsePacket( self, start ):
        end = start + 3
        version = int( self.binaryStr[start:end], 2 )
        self.versionSum += version
        start = end
        end = start+3
        packetType = int( self.binaryStr[start:end], 2 )

        # literal
        if packetType == 4:
            startBit = 1
            literalString = ""
            while startBit:
                startBit = int( self.binaryStr[end], 2)
                start = end + 1
                end = start + 4
                literalString += self.binaryStr[start:end]
            self._pushInQueue( int(literalString, 2), 0 )
            print(int(literalString, 2))
            return end
        else:
            self._pushInQueue(packetType, 1 )
            lengthTypeID = int( self.binaryStr[end], 2)
            if lengthTypeID == 0:
                start = end + 1
                end = start + 15
                subPacketLen = int( self.binaryStr[start:end], 2)
                subPacketEndIndex = end + subPacketLen
                while end < subPacketEndIndex:
                    end = self.ParsePacket( end )
                return end
            else:
                start = end + 1
                end = start + 11
                subPacketCount = int( self.binaryStr[start:end], 2)
                for _ in range(subPacketCount):
                    end = self.ParsePacket( end )
                return end


    def SolvePart1( self ):
        self.ParsePacket( 0 )
        return self.versionSum, self._compute()

if __name__ == '__main__':
    obj = Solution( "D:\\Github\\aoc_2021\\day16_input.txt" )
    versionSum, eval = obj.SolvePart1()
    print(" version sum : {}, {}".format(versionSum, eval))