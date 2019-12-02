with open('input') as file:
    program = file.read().replace('\n', '').split(',')
    for i in range(len(program)):
        program[i] = int(program[i])

    # 1202 program alarm
    program[1] = 12
    program[2] = 2

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
    print(program[0])
    file.close()
