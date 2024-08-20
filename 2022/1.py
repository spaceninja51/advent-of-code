def UnitTotals(inFile):
    """
    Takes in an inFile.txt and sums the numbers in a unit

    Units are blocks of lines grouped together

    Units are separated by \n
    """
    content = open(inFile)
    total = int(0)
    totals = []

    for i, line in enumerate(content):
        if line != '\n':
            total += int(line)
        else:
            totals.append(int(total))
            total = int(0)

    return totals

elfs = UnitTotals("./2022/1/in.txt")

p1 = sorted(elfs, reverse=True)[0]

print("Part 1 Solution: ",p1)

#Part 2

p2 = sum(sorted(elfs, reverse=True)[0:3])

print("Part 2 Solution: ",p2)
