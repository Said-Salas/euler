ways = [
    'x: 2 => y: -2', 
    'x: 1 => y: -1 => x: 1 => y: -1',
    ''
    ]


lattice = [
    [[0, 0], [1, 0], [2, 0]],
    [[0, -1], [1, -1], [2, -1]],
    [[0, -2], [1, -2], [2, -2]]
]
car = [0, 0]
pRoutes = 0
arrived = False

while arrived is not True: 
    for i in range (10):
        print(i)

    arrived = not arrived

print(arrived)