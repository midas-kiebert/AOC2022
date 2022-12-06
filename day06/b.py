import fileinput, re

string = input()

for i in range(14, len(string)):
    segment = string[i-14:i]
    if len(set(segment)) == 14:
        print(i)
        break