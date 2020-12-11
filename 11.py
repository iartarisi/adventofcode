example = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def read_input(lines):
    positions = []
    for line in lines:
        positions_line = []
        positions.append(positions_line)
        for c in line:
            positions_line.append(c)

    return positions


def one_step(positions):
    next_step = []
    for i, line in enumerate(positions):
        next_line = []
        next_step.append(next_line)
        for j, p in enumerate(line):
            if p == '.':
                next_line.append('.')
                continue

            adjacent_occupied = 0
            for x, y in [
                    (i-1, j-1), (i, j-1), (i+1, j-1), 
                    (i-1, j), (i+1, j), 
                    (i-1, j+1), (i, j+1), (i+1, j+1)]:
                if 0 <= x < len(positions) and 0 <= y < len(line):
                    # print(positions[x][y])
                    adjacent_occupied += 1 if positions[x][y] == '#' else 0

            if p == 'L' and adjacent_occupied == 0:
                next_line.append('#')
            elif p == '#' and adjacent_occupied >= 4:
                next_line.append('L')
            else:
                next_line.append(p)

    return next_step


def show(positions):
    for line in positions:
        for p in line:
            print(p, end="")
        print()
    print()


def stabilize(positions):
    prev = 0
    curr = positions
    while prev != curr:
        prev = curr
        curr = one_step(curr)


    return curr


def count_occupied(positions):
    return sum(p == '#' for line in positions for p in line)


pos = read_input(example.splitlines())
count_occupied(stabilize(pos))

with open('11.input') as f:
    silver = count_occupied(stabilize(read_input(f.readlines())))

print("silver: ", silver )
