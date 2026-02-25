with open("input.txt") as f:
    data = f.read().strip()

    floor = 0
    character_n = 1
    basement_reached = False

    for char in data:
        floor += 1 if char == '(' else -1

        if not basement_reached and floor < 0:
            # part 2 solution
            print(f'Basement reached after {character_n} instructions.')
            basement_reached = True
        else:
            character_n += 1

    # part 1 solution
    print(f'Santa ends up at {floor}.')
