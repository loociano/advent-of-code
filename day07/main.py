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


def _run(program, inputs, is_feedback=False, pc=0):
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


def _get_phase_permutations(phases):
    phase_perms = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_perms = new_perm
    return phase_perms


def part_one():
    max_thruster_signal = 0
    program = get_program('input')
    phase_perms = _get_phase_permutations(range(0, 5))
    for phase_perm in phase_perms:
        output = 0
        while len(phase_perm) > 0:
            output = _run(program.copy(), [phase_perm.pop(0), output])
        max_thruster_signal = max(max_thruster_signal, output)
    return max_thruster_signal


def _run_with_phase_setting(program, phase_setting):
    programs, pcs, inputs = [], [], []
    num_amps = len(phase_setting)
    amp_output = 0
    for i in range(0, num_amps):
        programs.append(program.copy())
        pcs.append(0)
        inputs.append([phase_setting[i]])
    while pcs[0] is not None:
        for i in range(0, num_amps):
            inputs[i].append(amp_output)
            amp_output, pc = _run(programs[i], inputs[i], True, pcs[i])
            pcs[i] = pc
    return inputs[0][0]


def part_two():
    max_thruster_signal = 0
    for phase_perm in _get_phase_permutations(range(5, 10)):
        max_thruster_signal = max(max_thruster_signal, _run_with_phase_setting(get_program('input'), phase_perm))
    return max_thruster_signal


print(part_one())  # 87138
print(part_two())  # 17279674
