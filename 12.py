example = """F10
N3
F7
R90
F11"""


directions = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

directions_order = 'NESW'


def navigate(turns):
    facing = 'E'
    x = 0
    y = 0
    for turn in turns:
        action, value = turn[0], turn[1:]
        value = int(value)

        if action == 'F':
            action = facing

        if action == 'R':
            turns = value // 90
            facing = directions_order[(directions_order.index(facing) + turns) % 4]
            continue
        elif action == 'L':
            turns = value // 90
            facing = directions_order[(directions_order.index(facing) - turns) % 4]
            continue

        movex, movey = directions[action]
        movex, movey = movex*value, movey*value

        x += movex
        y += movey
        print(x, y)

    return abs(x) + abs(y)

navigate(example.splitlines())

with open('12.input') as f:
    print(navigate(f.readlines()))
