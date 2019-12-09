def _decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def _get_op(program, pc, mode, offset, rel_base):
    if mode == 0:  # position mode
        return program[program[pc + offset]]
    if mode == 1:  # immediate mode
        return program[pc + offset]
    if mode == 2:  # relative mode
        return program[rel_base + program[pc + offset]]


def _get_op1(program, pc, mode, rel_base):
    return _get_op(program, pc, mode, 1, rel_base)


def _get_op2(program, pc, mode, rel_base):
    return _get_op(program, pc, mode, 2, rel_base)


def _get_op3(program, pc, mode, offset, rel_base):
    if mode == 2:
        return rel_base + program[pc + offset]
    return program[pc + offset]


def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run(program, input_id=0):
    diagnostic_code = 0
    pc = 0
    rel_base = 0
    mem = [0] * 100000
    for pos, intcode in enumerate(program):
        mem[pos] = intcode
    while pc < len(program):
        opcode_obj = _decode_opcode(mem[pc])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        op1_mode = opcode_obj[2]
        op2_mode = opcode_obj[1]
        op3_mode = opcode_obj[0]
        if opcode == 1 or opcode == 2:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3(mem, pc, op3_mode, 3, rel_base)] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            mem[_get_op3(mem, pc, op1_mode, 1, rel_base)] = input_id
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(mem, pc, op1_mode, rel_base)
            diagnostic_code = op1
            pc += 2
        elif opcode == 5 or opcode == 6:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else pc + 3
        elif opcode == 7:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 9:
            rel_base += _get_op1(mem, pc, op1_mode, rel_base)
            pc += 2
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return diagnostic_code


def part_one():
    return run(get_program('input'), 1)


print(part_one())
