side_length = 4
total_moves = side_length * 2
ways_list = []
way_count = 0

#sidelength * total moves + 2 = nWays ??
for first_r_index in range(total_moves - 3):
    for second_r_index in range(first_r_index + 1, total_moves - 2):
        for third_r_index in range(second_r_index + 1, total_moves - 1):
            for fourth_r_index in range(third_r_index + 1, total_moves):
                way = ["D"] * total_moves
                way[first_r_index] = "R"
                way[second_r_index] = "R"
                way[third_r_index] = "R"
                way[fourth_r_index] = "R"

                ways_list.append(way)
                way_count += 1

for way in ways_list:
    print(" ".join(way))

print("Ways:", way_count)
