class Intcode:
    pc = 0
    relative_base = 0
    mem = [0] * 100000

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

    def _get_op_address(self, mode, offset) -> int:
        if mode == 0:  # position mode
            return self.mem[self.pc + offset]
        if mode == 1:  # immediate mode
            return self.pc + offset
        if mode == 2:  # relative mode
            return self.relative_base + self.mem[self.pc + offset]

    def _get_op1(self, mode) -> int:
        return self.mem[self._get_op_address(mode, 1)]

    def _get_op2(self, mode) -> int:
        return self.mem[self._get_op_address(mode, 2)]

    def _get_op3_address(self, mode, offset) -> int:
        return self._get_op_address(mode, offset)


class RobotGrid:
    grid = {}
    robot_pos = tuple([0, 0])
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # up, right, down, left
    dir_index = 0

    def __init__(self, grid):
        self.grid = grid

    def get_panel_color(self) -> int:
        return int(self.grid.get(self.robot_pos, 0))

    def paint_panel(self, color: int) -> bool:
        newly_painted = self.grid.get(self.robot_pos) is None
        self.grid[self.robot_pos] = color
        return newly_painted

    def move_robot(self, next_dir: int):
        if next_dir == 1:  # turn right 90 degrees
            self.dir_index += 1
        elif next_dir == 0:  # turn left 90 degrees
            self.dir_index -= 1
        dir_vector = self.dirs[self.dir_index % len(self.dirs)]
        self.robot_pos = tuple([self.robot_pos[0] + dir_vector[0], self.robot_pos[1] + dir_vector[1]])


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
    robot_grid = RobotGrid(grid)
    painted_count = 0
    while True:
        curr_color = robot_grid.get_panel_color()
        color = vm.run(curr_color)
        if color is None:
            break
        painted_count += 1 if robot_grid.paint_panel(color) else 0
        robot_grid.move_robot(vm.run(curr_color))
    return painted_count


def part_two(filename):
    grid = {tuple([0, 0]): 1}  # starting panel is white
    grid_max_width = part_one(filename, grid)
    hull = [[' '] * grid_max_width for i in range(0, grid_max_width)]

    origin_x, origin_y = grid_max_width // 2, grid_max_width // 2
    for key, value in grid.items():
        if value == 1:
            hull[origin_y + key[1]][origin_x + key[0]] = '█'
    return _print_hull(hull)


print(part_one('input'))  # 2373
print(part_two('input'))  # PCKRLPUK
