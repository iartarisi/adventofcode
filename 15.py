example = """1,3,2"""


def solve(numbers):
    last_pos = {}
    for i, n in enumerate(numbers[:-1]):
        last_pos[int(n)] = i
    n = int(numbers[-1])
    i = len(numbers) - 1

    while i < 29999999:
        # print(n, i, last_pos)

        try:
            nn =  i - last_pos[n]
        except KeyError:
            nn = 0

        last_pos[n] = i
        i += 1
        n = nn

    return n

solve(example.split(','))
print(solve('2,1,3'.split(',')))
# print(solve('3,1,2'.split(',')))
print(solve('1,20,8,12,0,14'.split(',')))
