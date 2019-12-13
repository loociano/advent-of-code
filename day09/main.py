# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def _decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def _get_op_address(program, pc, mode, offset, rel_base):
    if mode == 0:  # position mode
        return program[pc + offset]
    if mode == 1:  # immediate mode
        return pc + offset
    if mode == 2:  # relative mode
        return rel_base + program[pc + offset]


def _get_op1(program, pc, mode, rel_base):
    return program[_get_op_address(program, pc, mode, 1, rel_base)]


def _get_op2(program, pc, mode, rel_base):
    return program[_get_op_address(program, pc, mode, 2, rel_base)]


def _get_op3_address(program, pc, mode, offset, rel_base):
    return _get_op_address(program, pc, mode, offset, rel_base)


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
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            mem[_get_op3_address(mem, pc, op1_mode, 1, rel_base)] = input_id
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
            break
        else:
            print('unknown opcode')
            break
    return diagnostic_code


def part_one():
    return run(get_program('input'), 1)


def part_two():
    return run(get_program('input'), 2)


print(part_one())  # 2870072642
print(part_two())  # 58534
