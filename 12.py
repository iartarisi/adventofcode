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


def navigate(steps):
    facing = 'E'
    x = 0
    y = 0
    for step in steps:
        action, value = step[0], step[1:]
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


def navigate_waypoint(steps, waypoint=(10, 1)):
    x = 0
    y = 0

    for step in steps:
        print(x, y, waypoint)

        action, value = step[0], step[1:]
        value = int(value)

        if action == 'F':
            x += value*waypoint[0]
            y += value*waypoint[1]
            continue

        try:
            movex, movey = directions[action]
        except KeyError:
            pass
        else:
            movex, movey = movex*value, movey*value
            waypoint = (waypoint[0] + movex, waypoint[1] + movey)
            continue

        if action == 'R':
            turns = value // 90
            for i in range(turns):
                waypoint = (waypoint[1], waypoint[0] * -1)
            continue
        elif action == 'L':
            turns = value // 90
            for i in range(turns):
                waypoint = (waypoint[1] * -1, waypoint[0])
            continue

    print(x, y, waypoint)
    return abs(x) + abs(y)

navigate_waypoint(example.splitlines())

with open('12.input') as f:
    print(navigate_waypoint(f.readlines()))
