# Output we want:
#   [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Version 1:
# Issue = iterator doesn't start over at each turn of the loop
# Output = [[2, 3]]

iterator = (i for i in range(1, 4))
matrix = [[x * y for y in iterator] for x in iterator]

# Version 2:
# Solution = don't use itertools

iterator = [i for i in range(1, 4)]
matrix = [[x * y for y in iterator] for x in iterator]
print(matrix)
