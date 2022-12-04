import fileinput

ans = 0
for line in fileinput.input():
    r1, r2 = line.strip().split(',')
    a1, b1 = map(int, r1.split('-'))
    a2, b2 = map(int, r2.split('-'))
    if (((a1 > a2) == (b1 < b2))) or (a1 == a2) or (b1 == b2):
        ans+=1
print(ans)