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

example1 = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""


def read_input(lines):
    positions = []
    for line in lines:
        positions_line = []
        positions.append(positions_line)
        for c in line:
            positions_line.append(c)

    return positions


def silver_step(positions):
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


def gold_step(positions):
    next_step = []
    for i, line in enumerate(positions):
        next_line = []
        next_step.append(next_line)
        for j, p in enumerate(line):
            # if i != 4 or j != 3:
            #     continue

            if p == '.':
                next_line.append('.')
                continue

            seen_occupied = 0
            # print("i:", i, "j:", j, end=" ")
            for x, y in [
                    (0, 1),
                    (1, 0),
                    (1, 1),
                    (-1, -1),
                    (-1, 0),
                    (0, -1),
                    (-1, 1),
                    (1, -1)
            ]:
                ii = i + x
                jj = j + y
                while 0 <= ii < len(positions) and 0 <= jj < len(line):
                    if positions[ii][jj] == '#':
                        # print(x, y, ii, jj)
                        seen_occupied += 1
                        break
                    if positions[ii][jj] == 'L':
                        break
                    ii += x
                    jj += y

            if p == 'L' and seen_occupied == 0:
                next_line.append('#')
            elif p == '#' and seen_occupied >= 5:
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


def stabilize(positions, step_func):
    prev = 0
    curr = positions
    while prev != curr:
        prev = curr
        curr = step_func(curr)

    return curr


def count_occupied(positions):
    return sum(p == '#' for line in positions for p in line)


pos = read_input(example.splitlines())
print("example:", count_occupied(stabilize(pos, gold_step)))

with open('11.input') as f:
    silver = count_occupied(stabilize(read_input(f.readlines()), silver_step))
with open('11.input') as f:
    gold = count_occupied(stabilize(read_input(f.readlines()), gold_step))

print("silver: ", silver)
print("gold: ", gold)
