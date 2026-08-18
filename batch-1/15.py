side_length = 20
total_moves = side_length * 2
ways_list = []
way_count = 0

for first_r_index in range(total_moves - 9):
    for second_r_index in range(first_r_index + 1, total_moves - 8):
        for third_r_index in range(second_r_index + 1, total_moves - 7):
            for fourth_r_index in range(third_r_index + 1, total_moves - 6):
                for fifth_r_index in range(fourth_r_index + 1, total_moves - 5):
                    for sixth_r_index in range(fifth_r_index + 1, total_moves - 4):
                        for seventh_r_index in range(sixth_r_index + 1, total_moves - 3):
                            for eighth_r_index in range(seventh_r_index + 1, total_moves - 2):
                                for ninth_r_index in range(eighth_r_index + 1, total_moves - 1):
                                    for tenth_r_index in range(ninth_r_index + 1, total_moves):
                                        way = ["D"] * total_moves
                                        way[first_r_index] = "R"
                                        way[second_r_index] = "R"
                                        way[third_r_index] = "R"
                                        way[fourth_r_index] = "R"
                                        way[fifth_r_index] = "R"
                                        way[sixth_r_index] = "R"
                                        way[seventh_r_index] = "R"
                                        way[eighth_r_index] = "R"
                                        way[ninth_r_index] = "R"
                                        way[tenth_r_index] = "R"

                                        ways_list.append(way)
                                        way_count += 1

for way in ways_list:
    print(" ".join(way))

print("Ways:", way_count)