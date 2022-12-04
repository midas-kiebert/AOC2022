import fileinput
totals = []
temp = 0
for line in fileinput.input():
    if line.strip():
        temp += int(line.strip())
    else:
        totals.append(temp)
        temp = 0
totals.append(temp)
totals.sort()
print(totals[-1]+totals[-2]+totals[-3])