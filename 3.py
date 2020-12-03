from copy import copy

def load_terrain(terrain):
    matrix = []
    i = 0
    j = 0
    for l in terrain:
        if not l:
            continue
        matrix.append([])
        for c in l:
            if c in ['.', '#']:
                matrix[i].append(c)
            j += 1
        i += 1
    return matrix

def down_slope(matrix, slope):
    trees = 0
    i = j = 0
    while True:
        i += slope[1]
        j += slope[0]
        if j >= len(matrix[0]):
            j -= len(matrix[0])

        try:
            o = matrix[i][j]
        except IndexError:
            break

        if o == '.':
            matrix[i][j] = 'O'
        elif o == '#':
            matrix[i][j] = 'X'
            trees += 1

    return trees


def run(terrain, slopes):
    matrix = load_terrain(terrain)

    answer = 1
    for slope in slopes:
        trees = down_slope(deepcopy(matrix), slope)
        answer *= trees

    return answer

def show(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='')
        print()


terrain = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

run(terrain.splitlines(), slopes=slopes)

with open('3.input') as f:
    print(run(f, slopes=slopes))


