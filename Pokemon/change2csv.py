f = open('names.txt', 'r', encoding='utf8')
lines = f.readlines()
f.close()

lines[0] = 'kr,jp,eng\n'
i = 0
while True:
    if lines[i] == '|-\n':
        lines.pop(i)
    else:
        if i > 0:
            lines[i] = lines[i].replace("||", ",")
            names = lines[i].split(",")
            names[1] = names[1].replace("[[", "")
            names[1] = names[1].replace("]]", "")
            lines[i] = ",".join([names[1], names[2], names[3] + '\n'])
        i += 1
    if i >= len(lines):
        break

f = open('names.csv', 'w', encoding='utf8')
for line in lines:
    f.write(line)
f.close()
