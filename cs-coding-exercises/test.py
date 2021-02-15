#!/bin/python3

arr = [[1,  2,  3, 4,  5,  6],
       [4,  5,  6, 7,  8,  9],
       [7,  8,  9, 10, 11, 12],
       [10, 11, 12,13, 14, 15]]
hourglasses = []
for i in range(len(arr)-2):
    print(i, arr[i])
    for j in range(len(arr[0])-2):
        hourglass = [arr[i][j], arr[i][j+1], arr[i][j+2],
                     arr[i+1][j+1],
                     arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
        if not hourglass in hourglasses:
            hourglasses.append(hourglass)

print()
for hg in hourglasses:
    print(hg)
sums = [sum(hg) for hg in hourglasses]
print(sums)