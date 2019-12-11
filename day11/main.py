def _decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def _get_op_address(mem, pc, mode, offset, rel_base):
    if mode == 0:  # position mode
        return mem[pc + offset]
    if mode == 1:  # immediate mode
        return pc + offset
    if mode == 2:  # relative mode
        return rel_base + mem[pc + offset]


def _get_op1(mem, pc, mode, rel_base):
    return mem[_get_op_address(mem, pc, mode, 1, rel_base)]


def _get_op2(mem, pc, mode, rel_base):
    return mem[_get_op_address(mem, pc, mode, 2, rel_base)]


def _get_op3_address(mem, pc, mode, offset, rel_base):
    return _get_op_address(mem, pc, mode, offset, rel_base)


def _get_panel_color(grid: dict, robot_pos: tuple):
    return grid.get('{} {}'.format(robot_pos[0], robot_pos[1]), 0)


def _paint_panel(grid: dict, robot_pos: tuple, color: int):
    key = '{} {}'.format(robot_pos[0], robot_pos[1])
    newly_painted = grid.get(key) is None
    grid[key] = color
    return newly_painted


def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run(mem: list, input: int, pc: int):
    output = None
    pc = pc
    rel_base = 0
    while True:
        opcode_obj = _decode_opcode(mem[pc])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        op1_mode = opcode_obj[2]
        op2_mode = opcode_obj[1]
        op3_mode = opcode_obj[0]
        if opcode == 1 or opcode == 2:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            mem[_get_op3_address(mem, pc, op1_mode, 1, rel_base)] = input
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(mem, pc, op1_mode, rel_base)
            output = op1
            pc += 2
            break
        elif opcode == 5 or opcode == 6:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else pc + 3
        elif opcode == 7:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 9:
            rel_base += _get_op1(mem, pc, op1_mode, rel_base)
            pc += 2
        elif opcode == 99:
            output = None
            break
        else:
            print('unknown opcode')
            break
    return output, pc


def part_one():
    program = get_program('input')
    mem = [0] * 100000
    for pos, intcode in enumerate(program):
        mem[pos] = intcode
    grid = {}
    pc = 0
    robot_pos = tuple([0, 0])
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # up, right, down, left
    curr_dir = 0  # default: up
    painted_count = 0
    while True:
        curr_color = _get_panel_color(grid, robot_pos)
        color, pc = run(mem, curr_color, pc)
        if color is None:
            break
        painted_count += 1 if _paint_panel(grid, robot_pos, color) else 0
        direction, pc = run(mem, curr_color, pc)
        if direction == 1:  # turn right 90 degrees
            curr_dir += 1
        elif direction == 0:  # turn left 90 degrees
            curr_dir -= 1
        vector = dirs[curr_dir % len(dirs)]
        robot_pos = tuple([robot_pos[0] + vector[0], robot_pos[1] + vector[1]])
    return painted_count


print(part_one())
