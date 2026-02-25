def move(coords, direction):
    if direction == 'west':
        return (coords[0]-1, coords[1])
    if direction == 'east':
        return (coords[0]+1, coords[1])
    if direction == 'north':
        return (coords[0], coords[1]+1)
    if direction == 'south':
        return (coords[0], coords[1]-1)

with open("input.txt") as f:
    input = f.read()

    # starting positions
    santa_coords = (0, 0)

    # grid for part 1
    visited_set = {santa_coords}

    move_count = 0
    for movement in input:
        # figure out direction and update position
        if (movement == '<'):
            santa_coords = move(santa_coords, 'west')
        elif (movement == '>'):
            santa_coords = move(santa_coords, 'east')
        elif (movement == '^'):
            santa_coords = move(santa_coords, 'north')
        else:
            santa_coords = move(santa_coords, 'south')

        # visited_set.add((x, y))
        visited_set.add(santa_coords)       

    print(f'Part 1 | Houses visited at least once: {len(visited_set)}')
        