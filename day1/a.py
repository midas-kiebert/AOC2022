import fileinput
ans = 0
temp = 0
for line in fileinput.input():
    if line.strip():
        temp += int(line.strip())
        ans = max(temp, ans)
    else:
        temp = 0
print(ans)