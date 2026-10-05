triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

triLen = len(triangle) - 2
column = 0
while triLen > -1:
    triangle[triLen][column] += max(triangle[triLen + 1][column], triangle[triLen + 1][column + 1])
    