from copy import deepcopy
from collections import namedtuple


class Matrix:
    def __init__(self, m):
        self.m = m
        self.ox = 0
        self.oy = 0


def add_line_above(matrix):
    columns = len(matrix.m[0])
    matrix.m.append(['.']*columns)

def add_column_right(matrix):
    for l in matrix.m:
        l.append('.')

def add_column_left(matrix):
    for l in matrix.m:
        l.insert(0, '.')
    matrix.oy += 1

def add_line_below(matrix):
    columns = len(matrix.m[0])
    new_line = ['.'] * columns
    matrix.m.insert(0, new_line)
    matrix.ox += 1

def mark_step(matrix, x, y, sign):
    try:
        matrix.m[x][y] = sign
    except IndexError:
        raise
    # if matrix[x][y] == '.':
    #     matrix[x][y] = sign
    # else:
    #     matrix[x][y] = 'X'

def extend_for(matrix, x, y):
    if y < 0:
        add_column_left(matrix)
        y = 0
    elif x < 0:
        add_line_below(matrix)
        x = 0
    if x + 1 > len(matrix.m):
        add_line_above(matrix)
    elif y + 1 > len(matrix.m[x]):
        add_column_right(matrix)

    return x, y

def make_step(matrix, direction, length, x, y):
    dirs = {
        'R': ('-', lambda x, y: (x, y + 1)),
        'U': ('|', lambda x, y: (x + 1, y)),
        'L': ('-', lambda x, y: (x, y - 1)),
        'D': ('|', lambda x, y: (x - 1, y)),
    }
    sign, funcxy = dirs[direction]
    for i in range(length):
        x, y = funcxy(x, y)
        x, y = extend_for(matrix, x, y)
        mark_step(matrix, x, y, sign)

    return x, y

def draw_line(matrix, steps):
    origin = [0, 0]
    x, y = origin
    for step in steps.split(','):
        direction, length = step[0], int(step[1:])

        x, y = make_step(matrix, direction, length, x, y)

    return matrix, origin

m = [['o']]
origin = [0, 0]

def cross_matrices(matrix1, matrix2):
    xs = max(len(matrix1.m), len(matrix2.m))
    ys = max(len(matrix1.m[0]), len(matrix2.m[0]))
    score = 1000*1000
    for i in range(xs):
        for j in range(ys):
            try:
                m1 = matrix1.m[i][j]
            except IndexError:
                continue

            if m1 == '.' or m1 == 'o':
                continue
            om1x = matrix1.ox - i
            om1y = matrix1.oy - j
            m2x = matrix2.ox - om1x
            m2y = matrix2.oy - om1y
            if m2x < 0 or m2y < 0:
                continue
            try:
                m2 = matrix2.m[m2x][m2y]
            except IndexError:
                continue

            if m2 != '.' and m2 != 'o':
                score = min(score, abs(om1x)+abs(om1y))

    return score

def show(matrix):
    print()
    for i in range(len(matrix.m)):
        for j in range(len(matrix.m[i])):
            print(matrix.m[len(matrix.m)-i-1][j], end='')
        print()

#show(matrix)

matrix1 = Matrix(deepcopy(m))
matrix2 = Matrix(deepcopy(m))

wire1 = 'R8,U5,L5,D13'
wire2 = 'U7,R6,D4,L4'

wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

with open('2019/3.input') as f:
    wire1 = f.readline().strip()
    wire2 = f.readline().strip()

print(wire1, wire2)

matrix1, origin1 = draw_line(matrix1, wire1)
matrix2, origin2 = draw_line(matrix2, wire2)
# show(matrix1)
# show(matrix2)
cross_matrices(matrix1, matrix2)
