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
from typing import Sequence
from aoc2019.src.common.intcode import read_intcode


def _decode_opcode(num: int) -> list:
  digits = [0, 0, 0, 0, 0]
  pos = len(digits) - 1
  while num > 0 and pos >= 0:
    digits[pos] = num % 10
    num //= 10
    pos -= 1
  return digits


def _get_op1(program: Sequence[int], pc: int, mode: int) -> int:
  return program[program[pc + 1]] if mode == 0 else program[pc + 1]


def _get_op2(program: Sequence[int], pc: int, mode: int) -> int:
  return program[program[pc + 2]] if mode == 0 else program[pc + 2]


def run(program: Sequence[int], input_id: int) -> int:
  program = list(program)
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


def part_one(program: str) -> int:
  return run(read_intcode(program), 1)


def part_two(program: str) -> int:
  return run(read_intcode(program), 5)
