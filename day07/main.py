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


def run(program, inputs, is_feedback=False, pc=0):
    diagnostic_code = 0
    pc = pc
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
            if len(inputs) == 0:
                raise Exception('no input!')
            program[program[pc + 1]] = inputs.pop(0)
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(program, pc, op1_mode)
            diagnostic_code = op1
            pc += 2
            if is_feedback:
                return diagnostic_code, pc
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
            if is_feedback:
                return diagnostic_code, None
            break
        else:
            print('unknown opcode')
            break
    return diagnostic_code


def permute(phases):
    phase_seq = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_seq:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_seq = new_perm
    return phase_seq


def part_one():
    max_thruster_signal = 0
    program = get_program('input')
    phase_seqs = permute(range(0, 5))
    for phase_seq in phase_seqs:
        output = 0
        while len(phase_seq) > 0:
            output = run(program.copy(), [phase_seq.pop(0), output])
        max_thruster_signal = max(max_thruster_signal, output)
    return max_thruster_signal


def part_two():
    max_thruster_signal = 0
    program = get_program('input')
    phase_seqs = permute(range(5, 10))
    output = 0
    for phase_seq in phase_seqs:
        programs = [program.copy(), program.copy(), program.copy(), program.copy(), program.copy()]
        pcs = [0, 0, 0, 0, 0]
        inputs = [[], [], [], [], []]
        for i in range(0, 5):
            inputs[i].append(phase_seq[i])
        while pcs[0] is not None:
            for i in range(0, 5):
                inputs[i].append(output)
                output, pc = run(programs[i], inputs[i], True, pcs[i])
                pcs[i] = pc
        max_thruster_signal = max(max_thruster_signal, inputs[0][0])
    return max_thruster_signal


print(part_one())  # 87138
print(part_two())  # 17279674
