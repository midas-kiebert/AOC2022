import fileinput
str1 = "ABC"
str2 = "XYZ"

def get_score(a, b):
    score = b + 1
    if a == b:
        score += 3
    elif (a+1) % 3 == b:
        score += 6
    return score


total_score = 0
for line in fileinput.input():
    line = line.strip().split()
    if not line:
        break
    a, b = str1.index(line[0]), str2.index(line[1])
    total_score += get_score(a, b)

print(total_score)
