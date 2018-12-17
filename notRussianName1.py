file = open("Perepis.txt", "r")
hmEarlierThan1978 = 0
for line in file:
    abc = line.split()
    if int(abc[3][6:10]) < 1978:
        hmEarlierThan1978 += 1
        print(abc[0], abc[1], abc[2])
print(hmEarlierThan1978)

print("Введи меня диапозон!")
fYear = int(input())
lYear = int(input())

file.close()
file = open("Perepis.txt", "r")

for line in file:
    abc = line.split()
    if fYear <= int(abc[3][6:10]) <= lYear:
        print(abc[0], abc[1], abc[2], abc[3])