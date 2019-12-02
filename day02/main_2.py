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


with open('input') as file:
    program = file.read().replace('\n', '').split(',')
    for i in range(len(program)):
        program[i] = int(program[i])
    file.close()
    for noun in range(100):
        for verb in range(100):
            if run_program(program.copy(), noun, verb) == 19690720:
                print(100 * noun + verb)
                break
