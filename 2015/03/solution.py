with open("input.txt") as f:
    input = f.read()

    # starting positions
    santa_coords = (0, 0)

    # grid for part 1
    visited_set = {santa_coords}

    move_count = 0
    for move in input:
        # figure out direction and update position
        if (move == '<'):
            santa_coords = (santa_coords[0] - 1, santa_coords[1])
        elif (move == '>'):
            santa_coords = (santa_coords[0] + 1, santa_coords[1])
        elif (move == '^'):
            santa_coords = (santa_coords[0], santa_coords[1] + 1)
        else:
            santa_coords = (santa_coords[0], santa_coords[1] - 1)

        # visited_set.add((x, y))
        visited_set.add(santa_coords)       

    print(f'Part 1 | Houses visited at least once: {len(visited_set)}')
        