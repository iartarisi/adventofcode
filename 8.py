example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def execute(inp):
    acc = 0
    executed = set()
    instructions = []
    for instruction in inp:
        operation, argument = instruction.split()
        argument = int(argument)
        instructions.append((operation, argument))


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



    return acc

execute(example.splitlines())
with open('8.input') as f:
    print(execute(f.readlines()))
