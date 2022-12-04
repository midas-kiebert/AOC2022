import fileinput
alphabet = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lines = [line.strip() for line in fileinput.input()]

s = 0
for i in range(0, len(lines), 3):
    l1,l2,l3 = (set(lines[i+j]) for j in range(3))
    s += alphabet.index(list((l1 & l2 & l3))[0])
print(s)