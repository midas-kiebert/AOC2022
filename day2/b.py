import fileinput
str1 = "ABC"
str2 = "XYZ"

def get_score(a, b):
    score = b * 3 + (a + b - 1) % 3 + 1
    return score


total_score = 0
for line in fileinput.input():
    line = line.strip().split()
    if not line:
        break
    a, b = str1.index(line[0]), str2.index(line[1])
    total_score += get_score(a, b)

print(total_score)
