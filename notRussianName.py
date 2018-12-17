file = open("Perepis.txt", "r")
hmEarlierThan1978 = 0
for line in file:
    yearFirstIndex = 0
    for index in range ( len(line) ):
        if( line[index] == '.'):
            yearFirstIndex = index + 4
            if int(line[yearFirstIndex:]) < 1978:
                hmEarlierThan1978 += 1
                print( line[:yearFirstIndex-10])
            break
print(hmEarlierThan1978)