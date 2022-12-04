import fileinput
alphabet = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = 0
for line in fileinput.input():
    line = line.strip()
    l1 = set(line[:len(line)//2])
    l2 = set(line[len(line)//2:])
    s += alphabet.index(list((l1 & l2))[0])
print(s)