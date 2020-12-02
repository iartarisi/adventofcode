from itertools import combinations

inputs = []
with open('Downloads/input') as f:
    [inputs.append(int(l)) for l in f]

x, y = next((i, j) for i, j in combinations(inputs, 2) if i + j == 2020)
part1 = x * y
print("Part1: ", part1)

x, y, z = next((i, j, k) for i, j, k in combinations(inputs, 3) if i + j + k == 2020)
part2 = x * y * z
print("Part2: ", part2)
