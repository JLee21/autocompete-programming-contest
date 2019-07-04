import fileinput

for line in fileinput.input():
  line = line.strip()
  print(line[::-1])
