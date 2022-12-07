import fileinput, re

lines = [line.strip() for line in fileinput.input()]

CUTOFF = 100000

parent = {"/": "/"}
size = {"/": 0}

directory = "/"

for line in lines:
    if line[0:4] == "$ cd":
        inp = line[5:]
        if inp == "..":
            directory = parent[directory]
        else:
            if directory == "/":
                new_directory = inp
            else:
                new_directory = f"{directory}/{inp}"
            parent[new_directory] = directory
            directory = new_directory
    elif line[0] == "$" or line[0] == "d":
        continue
    else:
        size[directory] = size.get(directory, 0) + int(line.split()[0])
        temp = directory
        while temp != '/':
            size[parent[temp]] = size.get(parent[temp], 0) + int(line.split()[0])
            temp = parent[temp]
print(sum([size[a] for a in size if size[a] <= CUTOFF]))