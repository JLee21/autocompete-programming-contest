import fileinput
for line in fileinput.input():
    s = line

arr = list(map(int, s))
total_candy = 0


def get_slice_total(a):
    i = 0
    slice_total = 0
    while a[i] < 0:
        i += 1
    left = i

    j = len(a) - 1
    while a[j] < 0:
        j -= 1

    right = j

    if left == right:
        return 0

    for k in range(left+1, right):
        if a[k] < 0:
            slice_total += 1

    return slice_total


while any([x >= 0 for x in arr]):
    print(arr, get_slice_total(arr))
    total_candy += get_slice_total(arr)
    arr = [x-1 for x in arr]

print(total_candy)
