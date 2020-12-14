import re


example = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


def calculate(lines):
    mem = {}
    bitmask = {}
    for line in lines:
        if line.startswith('mask'):
            bitmask = {}
            maskstring = re.match('mask = (\w+)', line).groups()[0]
            for i, c in enumerate(maskstring):
                if c != 'X':
                    bitmask[35 - i] = int(c)
        else:
            pos, value = re.match('mem\[(\d+)\] = (\d+)', line).groups()
            value = int(value) # format(int(value), '032b')
            print(value)
            for b, v in bitmask.items():
                print("bv", b, v)
                if v == 0:
                    value = value & ~(1 << b)
                elif v == 1:
                    value = value | 1 << b
            mem[pos] = value

    return sum(mem.values())

calculate(example.splitlines())
with open('14.input') as f:
    print(calculate(f.readlines()))

