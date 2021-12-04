import collections
import re

def ParseFile( filePath ):
    print( '* Loading\t%s' % filePath )
    tickets = []
    bingoNumbers = []
    with open( filePath, 'r', newline='' ) as fileHandle:
        lines = fileHandle.readlines()
        for lineNum, line in enumerate(lines):
            #read first line with bingo random sequence
            if lineNum == 0:
                bingoNumbers = [ int(entry) for entry in line.strip().split(",") ]
            elif line == "\r\n":
                continue
            else:
                tickets.append( [int(entry) for entry in re.split( '\s+', line.strip() ) ] )
    return bingoNumbers, tickets

def ComputePart1( bingoNums, tickets ):
    r = len(tickets)
    c = len(tickets[0])
    ticketCount = r//c

    ticketsRowTally = [0]*r
    ticketsColTally = [[0]*c for i in range(ticketCount) ]

    for index, num in enumerate(bingoNums):
        for i in range(r):
            for j in range(c):
                if tickets[i][j] == num:
                    tickets[i][j] = -1
                    ticketNum = i//c
                    ticketsRowTally[i]+=1
                    ticketsColTally[ticketNum][j]+=1
                    if ticketsRowTally[i] == c or ticketsColTally[ticketNum][j] == c:
                        return num, ticketNum, tickets

def ComputeScore( bingoNum, ticketNum, tickets ):
    c = len(tickets[0])
    startRow = ticketNum * c
    endRow = startRow + c
    unMarkedNumSum = 0
    for row in range( startRow, endRow ):
        for col in range(0, c ):
            if tickets[row][col] != -1:
                unMarkedNumSum += tickets[row][col]
    
    return unMarkedNumSum*bingoNum

def ComputePart2( bingoNums, tickets ):
    r = len(tickets)
    c = len(tickets[0])
    ticketCount = r//c

    ticketsRowTally = [0]*r
    ticketsColTally = [[0]*c for i in range(ticketCount) ]
    ticketsCaimed = [0]*ticketCount
    winningTicketCount = 0

    for index, num in enumerate(bingoNums):
        for i in range(r):
            for j in range(c):
                if tickets[i][j] == num:
                    tickets[i][j] = -1
                    ticketNum = i//c
                    ticketsRowTally[i]+=1
                    ticketsColTally[ticketNum][j]+=1
                    if ticketsRowTally[i] == c or ticketsColTally[ticketNum][j] == c:
                        if ticketsCaimed[ticketNum] == 0:
                            ticketsCaimed[ticketNum] = 1
                            winningTicketCount += 1
                            if winningTicketCount == ticketCount:
                                return num, ticketNum, tickets

if __name__ == '__main__':
    numDrawSeq, tickets = ParseFile( "D:\\Github\\aoc_2021\\day4_sample.csv" )

    part1Tickets = [row[:] for row in tickets]
    winningNum, ticketNum, part1Tickets = ComputePart1( numDrawSeq, part1Tickets )
    scorePart1 = ComputeScore( winningNum, ticketNum, part1Tickets )

    part2Tickets = [row[:] for row in tickets]
    winningNum, ticketNum, part2Tickets = ComputePart2( numDrawSeq, part2Tickets )
    scorePart2 = ComputeScore( winningNum, ticketNum, part2Tickets )

    print("Output 1:{}".format(scorePart1))
    print("Output 1:{}".format(scorePart2))