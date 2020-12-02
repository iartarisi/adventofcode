import sys



def addition(mem, x, y, z):
    mem[z] = mem[x] + mem[y]

def multiplication(mem, x, y, z):
    mem[z] = mem[x] * mem[y]

# def halt():
#     print(memory[0])
#     sys.exit()

instructions = {
    1: (addition, 3),
    2: (multiplication, 3),
    99: (None, 0)
}

with open('2.input') as f:
    memory = [int(i) for i in f.read().split(',')]


# memory = [1,1,1,4,99,5,6,0,99]
# memory = [2,4,4,5,99,0]


def solve(memory, noun, verb):
    # print(memory, noun,verb)

    memory[1] = noun
    memory[2] = verb

    i = 0
    while True:
        try:
            instruction, params_len = instructions[memory[i]]
        except KeyError:
            return None

        if instruction is None:
            break

        params = [memory[i+j+1] for j in range(params_len)]
        instruction(memory, *params)

        i += 1 + params_len

    return memory[0]

# print(solve(memory))
# print(memory)


def search(mem, x):
    for noun in range(99):
        for verb in range(99):
            if solve(mem[:], noun, verb) == x:
                return 100 * noun + verb

print(memory)
print(search(memory[:], 19690720))
