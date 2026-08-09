from itertools import combinations

grid_size = 2
total_moves = grid_size * 2
positions = range(total_moves)

right_position_choices = combinations(positions, grid_size)

for right_positions in right_position_choices:
    path = ""

    for current_position in positions:
        if current_position in right_positions:
            path += "R"
        else:
            path += "D"

    print(path)