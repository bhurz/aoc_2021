import csv

def ParseCsv( filePath ):
    print( '* Loading\t%s' % filePath )
    fileData = []

    with open( filePath, 'r', newline='' ) as fileHandle:
        reader = csv.reader( fileHandle )
        for row in reader:
            fileData.append(int(row[0]))

    return fileData

def CountDepthIncreaseWondows( fileData, windowSize ):
    count = 0
    for i in range( len(fileData) - windowSize ):
        if fileData[i] < fileData[i+windowSize]:
            count += 1

    return count
if __name__ == '__main__':
    fileData = ParseCsv( "D:\\advent_of_code\\AOC_2021\\day1_sample.csv" )
    print( 'Single Level increment {}'.format( CountDepthIncreaseWondows(fileData, 1) ) )
    print( 'Window Level increment {}'.format( CountDepthIncreaseWondows(fileData, 3) ) )
