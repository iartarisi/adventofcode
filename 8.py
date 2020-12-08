example = """nip +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def load_instructions(inp):
    instructions = []
    for instruction in inp:
        operation, argument = instruction.split()
        argument = int(argument)
        instructions.append((operation, argument))

    return instructions


def execute(instructions):
    acc = 0
    executed = set()

    i = 0
    while i not in executed:
        executed.add(i)
        (operation, argument) = instructions[i]

        if operation == 'nop':
            i += 1
            continue
        if operation == 'acc':
            acc += argument
            i += 1
            continue
        if operation == 'jmp':
            i += argument
            continue

    print(i)
    if i == len(instructions) - 1:
        return True, acc
    else:
        return False, acc


instructions = load_instructions(example.splitlines())
execute(instructions)

with open('8.input') as f:
    instructions = load_instructions(f.readlines())
    print(execute(instructions))
