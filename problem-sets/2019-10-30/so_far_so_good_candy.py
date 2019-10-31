import fileinput
for line in fileinput.input():
    s = line

arr = list(map(int, s))
i = 0
total_candy = 0

while i < len(arr)-1:
    while arr[i+1] >= arr[i]:
        i += 1
    left = arr[i]
    j = i+1
    valley_total = 0
    while arr[j] < left and j < len(arr):
        valley_total += (left - arr[j])
        j += 1
    if j != len(arr):
        total_candy += valley_total
    i = j


print(total_candy)
