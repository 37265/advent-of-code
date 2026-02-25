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

    # starting position for part 1
    santa_coords = (0, 0)
    # starting positions for part 2
    coop_santa_coords = (0, 0)
    coop_robo_coords = (0, 0)

    # grid for part 1
    visited_set = {santa_coords}
    # grids for part 2
    santa_visited_set = {coop_santa_coords}
    robo_visited_set = set()

    movement_count = 1
    for movement in input:
        # move Santa to new location
        santa_coords = move(santa_coords, movement)
        # update grid with new location
        visited_set.add(santa_coords)

        # part 2
        if movement_count % 2 == 0:
            coop_robo_coords = move(coop_robo_coords, movement)
            robo_visited_set.add(coop_robo_coords)
        else:
            coop_santa_coords = move(coop_santa_coords, movement)
            santa_visited_set.add(coop_santa_coords)
        movement_count += 1       

    print(f'Part 1 | Houses visited at least once: {len(visited_set)}')
    print('Part 2 | Santa and Robo-Santa together visited',
          f'{len(santa_visited_set | robo_visited_set)} houses at least once.')
        