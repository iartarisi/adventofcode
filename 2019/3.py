from collections import defaultdict

# def draw_one(matrix, x, y, sign):
#     if matrix[x][y]
def add_line(matrix):
    columns = len(matrix[0])
    matrix.append(['.']*columns)

def add_column(matrix):
    for l in matrix:
        l.append('.')

def draw_line(matrix, steps):
    x, y = (0, 0)
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
                    add_column(matrix)

                if matrix[x][y] == '.':
                    matrix[x][y] = '-'
                else:
                    matrix[x][y] = 'X'
        elif direction == 'U':
            for i in range(length):
                # assume that the left side has been drawn
                x += 1
                try:
                    matrix[x]
                except IndexError:
                    add_line(matrix)

                if matrix[x][y] == '.':
                    matrix[x][y] = '|'
                else:
                    matrix[x][y] = 'X'
        elif direction == 'L':
            for i in range(length):
                y -= 1
                if matrix[x][y] == '.':
                    matrix[x][y] = '-'
                else:
                    matrix[x][y] = 'X'
        elif direction == 'D':
            for i in range(length):
                x -= 1
                if matrix[x][y] == '.':
                    matrix[x][y] = '|'
                else:
                    matrix[x][y] = 'X'

        matrix[x][y]

wire1 = 'R8,U5,L5,D3' #',L5,D3'
wire2 = 'U7,R6,D4,L4'

wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
matrix = [['o']]
draw_line(matrix, wire1)
draw_line(matrix, wire2)

def show(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[len(matrix)-i-1][j], end='')
        print()

show(matrix)
