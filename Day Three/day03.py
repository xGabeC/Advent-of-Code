from functools import reduce

def getTreesEncountered(slope_x, slope_y, inputArray):
    x, y = 0,0 
    counter = 0
    while y < len(inputArray) - slope_y:
        x += slope_x
        y += slope_y
        if inputArray[y][ x % len(inputArray[y]) ] == '#':
            counter += 1
        # print(y % len(inputArray[x]))
        # print(x,y)
        print(inputArray[y][ x % len(inputArray[y]) ])
    return counter


inputArray = [ x.strip() for x in open('input03.txt').readlines() ]
print(getTreesEncountered(1, 3, inputArray))
print(reduce(lambda prev, slope: prev * getTreesEncountered(slope[0], slope[1], inputArray), [(1,1), (3,1), (5,1), (7,1), (1,2) ], 1))