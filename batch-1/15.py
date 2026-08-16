side_length = 2
total_moves = side_length * 2
ways_list = []
way_count = 0

# The first R stays fixed while the second R shifts to the right.
for first_r_index in range(total_moves - 1):
    for second_r_index in range(first_r_index + 1, total_moves):
        way = ["D"] * total_moves
        way[first_r_index] = "R"
        way[second_r_index] = "R"

        ways_list.append(way)
        way_count += 1

for way in ways_list:
    print(" ".join(way))

print("Ways:", way_count)
