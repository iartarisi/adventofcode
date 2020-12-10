example1 = """16
10
15
5
1
11
7
19
6
12
4
"""

example2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

def read_input(lines):
    adapters = []
    for i in lines:
        adapters.append(int(i))

    return sorted(adapters)


def measure_jolts(adapters):
    ones = 0
    threes = 0
    prev = 0
    for a in adapters:
        print(a - prev)
        if a - prev == 1:
            ones += 1
        elif a - prev == 3:
            threes += 1
        prev = a

    # builtin adapter
    threes += 1
    print(ones, threes)
    return ones * threes


adapters = read_input(example1.splitlines())
adapters = read_input(example2.splitlines())
print(measure_jolts(adapters))

with open('10.input') as f:
    adapters = read_input(f.readlines())
    print(measure_jolts(adapters))
