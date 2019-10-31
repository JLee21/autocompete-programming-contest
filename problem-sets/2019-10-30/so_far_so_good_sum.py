import fileinput
for line in fileinput.input():
    _sum = sum([int(x) for x in line])
    print(_sum)
