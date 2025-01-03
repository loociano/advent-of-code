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


def run_program(program: Sequence[int], noun: int, verb: int) -> int:
  program = list(program)
  program[1] = noun
  program[2] = verb
  pc = 0
  while pc < len(program):
    opcode = program[pc]
    op1 = program[program[pc + 1]]
    op2 = program[program[pc + 2]]
    dest = program[pc + 3]
    if opcode == 1 or opcode == 2:
      program[dest] = op1 + op2 if opcode == 1 else op1 * op2
      pc += 4
    elif opcode == 99:
      break
    else:
      print('unknown opcode')
      break
  return program[0]


def part_one(program: str) -> int:
  return run_program(read_intcode(program), 12, 2)


def part_two(program: str, output: int) -> int:
  program = read_intcode(program)
  for noun in range(100):
    for verb in range(100):
      if run_program(program, noun, verb) == output:
        return 100 * noun + verb
  return -1
