from copy import deepcopy

example = """nop +0
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
        try:
            operation, argument = instructions[i]
        except IndexError:
            if i == len(instructions):
                return True, acc
            else:
                return False, acc

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

    return False, acc

def switch_and_find(instructions, o1, o2):
    for i, (operation, argument) in enumerate(instructions):
        if operation == o1:
            insts = deepcopy(instructions)
            insts[i] = (o2, argument)
            success, acc = execute(insts)

            if success:
                return acc



instructions = load_instructions(example.splitlines())
# execute(instructions)

with open('8.input') as f:
    instructions = load_instructions(f.readlines())

print(instructions)


print(execute(instructions))
print(switch_and_find(instructions, 'nop', 'jmp'))
print(switch_and_find(instructions, 'jmp', 'nop'))
