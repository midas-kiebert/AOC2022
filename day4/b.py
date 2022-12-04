import fileinput

ans = 0
for line in fileinput.input():
    r1, r2 = line.strip().split(',')
    a1, b1 = map(int, r1.split('-'))
    a2, b2 = map(int, r2.split('-'))
    ans += ((b1 >= a2) and (b2 >= a1))
print(ans)