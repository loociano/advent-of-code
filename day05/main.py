def _decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def _get_op1(program, pc, mode):
    return program[program[pc + 1]] if mode == 0 else program[pc + 1]


def _get_op2(program, pc, mode):
    return program[program[pc + 2]] if mode == 0 else program[pc + 2]


def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run(program, input_id):
    diagnostic_code = 0
    pc = 0
    while pc < len(program):
        opcode_obj = _decode_opcode(program[pc])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        op1_mode = opcode_obj[2]
        op2_mode = opcode_obj[1]
        if opcode == 1 or opcode == 2:
            op1, op2 = _get_op1(program, pc, op1_mode), _get_op2(program, pc, op2_mode)
            dest = program[pc + 3]
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            program[program[pc + 1]] = input_id
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(program, pc, op1_mode)
            diagnostic_code = op1
            pc += 2
        elif opcode == 5 or opcode == 6:
            op1, op2 = _get_op1(program, pc, op1_mode), _get_op2(program, pc, op2_mode)
            pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else pc + 3
        elif opcode == 7:
            op1, op2 = _get_op1(program, pc, op1_mode), _get_op2(program, pc, op2_mode)
            program[program[pc + 3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8:
            op1, op2 = _get_op1(program, pc, op1_mode), _get_op2(program, pc, op2_mode)
            program[program[pc + 3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return diagnostic_code


print(run(get_program('input'), 1))  # 9025675
print(run(get_program('input'), 5))  # 11981754