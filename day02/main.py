def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    pc = 0
    while pc < len(program):
        opcode = program[pc]
        op1 = program[program[pc + 1]]
        op2 = program[program[pc + 2]]
        dest = program[pc + 3]
        if opcode == 1 or opcode == 2:
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return program[0]


def part_one():
    return run_program(get_program('input'), 12, 2)


def part_two(output):
    program = get_program('input')
    for noun in range(100):
        for verb in range(100):
            if run_program(program.copy(), noun, verb) == output:
                return 100 * noun + verb
    return 'not found'


print(part_one())
print(part_two(19690720))
