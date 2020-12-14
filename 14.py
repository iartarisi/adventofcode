import re


example = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

example2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

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


def expand_bitstring(bs):
    outputs = ['']
    for c in bs:
        if c == 'X':
            outputs = [o + y for o in outputs for y in ['0', '1']]
        else:
            outputs = [o + c for o in outputs]

    return outputs


def calculate_v2(lines):
    mem = {}
    bitmask = {}
    maskstring = None
    for line in lines:
        if line.startswith('mask'):
            maskstring = re.match('mask = (\w+)', line).groups()[0]
        else:
            pos, value = re.match('mem\[(\d+)\] = (\d+)', line).groups()
            posbits = format(int(pos), '036b')
            new_pos = []
            # print(posbits)
            # print(maskstring)
            for m, v in zip(maskstring, posbits):
                if m == '0':
                    new_pos.append(v)
                else:
                    new_pos.append(m)
            expanded = expand_bitstring(''.join(new_pos))
            for e in expanded:
                mem[e] = int(value)
            # print(expanded)

    return sum(mem.values())



calculate_v2(example2.splitlines())
with open('14.input') as f:
    print(calculate_v2(f.readlines()))

