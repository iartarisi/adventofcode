from itertools import combinations

test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def find_impostor(lines, preamble_size):
    preamble = []
    for n in lines:
        print(preamble, n)
        n = int(n)
        if len(preamble) >= preamble_size:
            for p, r in combinations(preamble, 2):
                if p + r == n:
                    break
            else:
                return n
            preamble.pop(0)

        preamble.append(n)



print(find_impostor(test_input.splitlines(), 5))
with open('9.input') as f:
    find_impostor(f.readlines(), 25)

