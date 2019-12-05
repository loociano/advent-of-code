def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def run_program(program, input):
    output = 0
    pc = 0
    while pc < len(program):
        opcode_obj = decode_opcode(program[pc])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        param1_mode = opcode_obj[2]
        param2_mode = opcode_obj[1]
        if opcode == 1 or opcode == 2:
            op1 = program[program[pc + 1]] if param1_mode == 0 else program[pc + 1]
            op2 = program[program[pc + 2]] if param2_mode == 0 else program[pc + 2]
            dest = program[pc + 3]
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            program[program[pc + 1]] = input
            pc += 2
        elif opcode == 4:
            op1 = program[program[pc + 1]] if param1_mode == 0 else program[pc + 1]
            output = op1
            pc += 2
        elif opcode == 5 or opcode == 6:
            op1 = program[program[pc + 1]] if param1_mode == 0 else program[pc + 1]
            op2 = program[program[pc + 2]] if param2_mode == 0 else program[pc + 2]
            pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else pc + 3
        elif opcode == 7:
            op1 = program[program[pc + 1]] if param1_mode == 0 else program[pc + 1]
            op2 = program[program[pc + 2]] if param2_mode == 0 else program[pc + 2]
            program[program[pc + 3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8:
            op1 = program[program[pc + 1]] if param1_mode == 0 else program[pc + 1]
            op2 = program[program[pc + 2]] if param2_mode == 0 else program[pc + 2]
            program[program[pc + 3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return output


def part_one():
    return run_program(get_program('input'), 1)


def part_two():
    return run_program(get_program('input'), 5)


print(part_one())
print(part_two())
