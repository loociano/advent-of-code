class Intcode:

    mem = [0] * 100000
    pc = 0
    relative_base = 0

    def __init__(self, program: list):
        self.program = program
        for pos, intcode in enumerate(program):
            self.mem[pos] = intcode

    def run(self, input_val: int) -> int:
        output = None
        while True:
            opcode_obj = self._decode_opcode()
            opcode = opcode_obj[3] * 10 + opcode_obj[4]
            op1_mode = opcode_obj[2]
            op2_mode = opcode_obj[1]
            op3_mode = opcode_obj[0]
            if opcode == 1 or opcode == 2:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = op1 + op2 if opcode == 1 else op1 * op2
                self.pc += 4
            elif opcode == 3:
                self.mem[self._get_op3_address(op1_mode, 1)] = input_val
                self.pc += 2
            elif opcode == 4:
                op1 = self._get_op1(op1_mode)
                output = op1
                self.pc += 2
                break
            elif opcode == 5 or opcode == 6:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else self.pc + 3
            elif opcode == 7:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = 1 if op1 < op2 else 0
                self.pc += 4
            elif opcode == 8:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = 1 if op1 == op2 else 0
                self.pc += 4
            elif opcode == 9:
                self.relative_base += self._get_op1(op1_mode)
                self.pc += 2
            elif opcode == 99:
                output = None
                break
            else:
                print('unknown opcode')
                break
        return output

    def _decode_opcode(self) -> list:
        opcode = self.mem[self.pc]
        digits = [0, 0, 0, 0, 0]
        pos = len(digits) - 1
        while opcode > 0 and pos >= 0:
            digits[pos] = opcode % 10
            opcode //= 10
            pos -= 1
        return digits

    def _get_op_address(self, mode, offset):
        if mode == 0:  # position mode
            return self.mem[self.pc + offset]
        if mode == 1:  # immediate mode
            return self.pc + offset
        if mode == 2:  # relative mode
            return self.relative_base + self.mem[self.pc + offset]

    def _get_op1(self, mode):
        return self.mem[self._get_op_address(mode, 1)]

    def _get_op2(self, mode):
        return self.mem[self._get_op_address(mode, 2)]

    def _get_op3_address(self, mode, offset):
        return self._get_op_address(mode, offset)


def _make_key(x: int, y: int):
    return '{} {}'.format(x, y)


def _get_panel_color(grid: dict, robot_pos: tuple):
    return int(grid.get(_make_key(robot_pos[0], robot_pos[1]), 0))


def _paint_panel(grid: dict, robot_pos: tuple, color: int):
    key = _make_key(robot_pos[0], robot_pos[1])
    newly_painted = grid.get(key) is None
    grid[key] = color
    return newly_painted


def _get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def _print_hull(hull: list):
    hull_str = []
    for row in hull:
        hull_str.append(''.join(row))
    return '\n'.join(hull_str)


def part_one(filename: str, grid=None):
    if grid is None:
        grid = {}
    vm = Intcode(_get_program(filename))
    robot_pos = tuple([0, 0])
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # up, right, down, left
    curr_dir = 0  # default: up
    painted_count = 0
    while True:
        curr_color = _get_panel_color(grid, robot_pos)
        color = vm.run(curr_color)
        if color is None:
            break
        painted_count += 1 if _paint_panel(grid, robot_pos, color) else 0
        direction = vm.run(curr_color)
        if direction == 1:  # turn right 90 degrees
            curr_dir += 1
        elif direction == 0:  # turn left 90 degrees
            curr_dir -= 1
        dir_vector = dirs[curr_dir % len(dirs)]
        robot_pos = tuple([robot_pos[0] + dir_vector[0], robot_pos[1] + dir_vector[1]])
    return painted_count


def part_two(filename):
    grid = {_make_key(0, 0): 1}  # starting panel is white
    grid_width = part_one(filename, grid)
    hull = []
    for i in range(0, grid_width):
        hull.append([' '] * grid_width)

    x = grid_width // 2
    y = x
    for key, value in grid.items():
        dx, dy = key.split(' ')
        if value == 1:
            hull[y + int(dy)][x + int(dx)] = '█'
    return _print_hull(hull)


print(part_one('input'))
print(part_two('input'))
