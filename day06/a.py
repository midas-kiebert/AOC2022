string = input()

for i in range(4, len(string)):
    segment = string[i-4:i]
    if len(set(segment)) == 4:
        print(i)
        break