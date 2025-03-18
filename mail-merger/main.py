

with open("letter.txt", "rt") as fin:
    with open("out.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('A', 'Orange'))


lines = open("names.txt", "r")
names_list = []

for line in lines:
    line.strip('\n')
    item = line
    names_list.append(item)
    #['A\n', 'B\n', 'C\n', 'D\n', 'E\n', 'F\n', 'G']

    with open("letter.txt", "rt") as fin:
        with open(f"letter_{item}.txt", "wt") as fout:
            for line1 in fin:
                fout.write(line1.replace('[name]', item))
