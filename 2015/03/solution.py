def move(coords, direction):
    if direction == '<':
        return (coords[0]-1, coords[1])
    if direction == '>':
        return (coords[0]+1, coords[1])
    if direction == '^':
        return (coords[0], coords[1]+1)
    if direction == 'v':
        return (coords[0], coords[1]-1)

with open("input.txt") as f:
    input = f.read()

    # starting positions
    santa_coords = (0, 0)

    # grid for part 1
    visited_set = {santa_coords}

    move_count = 0
    for movement in input:
        santa_coords = move(santa_coords, movement)

        # visited_set.add((x, y))
        visited_set.add(santa_coords)       

    print(f'Part 1 | Houses visited at least once: {len(visited_set)}')
        