from collections import defaultdict


def add_line_above(matrix):
    columns = len(matrix[0])
    matrix.append(['.']*columns)

def add_column_right(matrix):
    for l in matrix:
        l.append('.')

def add_column_left(matrix):
    for l in matrix:
        l.insert(0, '.')
    origin[1] = origin[1] + 1

def add_line_below(matrix):
    columns = len(matrix[0])
    new_line = ['.'] * columns
    matrix.insert(0, new_line)
    origin[0] = origin[0] + 1

def mark_step(matrix, x, y, sign):
    if matrix[x][y] == '.':
        matrix[x][y] = sign
    else:
        matrix[x][y] = 'X'


def draw_line(matrix, steps):
    x, y = origin
    for step in steps.split(','):
        print(step)
        print(x, y)
        direction, length = step[0], int(step[1:])

        if direction == 'R':
            for i in range(length):
                y += 1
                try:
                    matrix[x][y]
                except IndexError:
                    add_column_right(matrix)

                mark_step(matrix, x, y, '-')
        elif direction == 'U':
            for i in range(length):
                x += 1
                try:
                    matrix[x]
                except IndexError:
                    add_line_above(matrix)

                mark_step(matrix, x, y, '|')
        elif direction == 'L':
            for i in range(length):
                if y == 0:
                    add_column_left(matrix)
                else:
                    y -= 1

                mark_step(matrix, x, y, '-')
        elif direction == 'D':
            for i in range(length):
                if x == 0:
                    add_line_below(matrix)
                else:
                    x -= 1

                mark_step(matrix, x, y, '|')

        matrix[x][y]


wire1 = 'R8,U5,L5,D3' #',L5,D3'
wire2 = 'U7,R6,D4,L4'

# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# wire1 = 'U2,L5,U2,R3'
# wire2 = 'R7,D2'

matrix = [['o']]
origin = [0, 0]

draw_line(matrix, wire1)
draw_line(matrix, wire2)

def show(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[len(matrix)-i-1][j], end='')
        print()

show(matrix)
