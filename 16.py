from functools import partial
import re

example = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


def collect_valid_values(line):
    valid_ranges = re.match('.*: (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
    return (
        list(range(int(valid_ranges[0]), int(valid_ranges[1]) + 1)) +
        list(range(int(valid_ranges[2]), int(valid_ranges[3]) + 1)))


def collect_invalids(valids, line):
    return [int(i) for i in line.split(',') if int(i) not in valids]


def process_input(lines):
    myticket = set()
    valids = set()
    invalid = []
    section = valids.update
    func = collect_valid_values
    for line in lines:
        line = line.strip()
        if line in ['', '\n']:
            continue

        if line == 'nearby tickets:':
            section = invalid.extend
            func = partial(collect_invalids, valids)
            continue

        if line == 'your ticket:':
            section = lambda x: myticket.add(x)
            func = lambda x: x
            continue

        section(func(line))

    return valids, myticket, invalid

def silver(lines):
    valid, myticket, invalid = process_input(lines)

    print(valid)
    print(myticket)
    print(invalid)

    return sum(invalid)

silver(example.splitlines())

with open('16.input') as f:
    print(silver(f.readlines()))

