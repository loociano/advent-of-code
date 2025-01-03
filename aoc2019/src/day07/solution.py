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


def decode_opcode(num):
  digits = [0, 0, 0, 0, 0]
  pos = len(digits) - 1
  while num > 0 and pos >= 0:
    digits[pos] = num % 10
    num //= 10
    pos -= 1
  return digits


def get_op1(program, pc, mode):
  return program[program[pc + 1]] if mode == 0 else program[pc + 1]


def get_op2(program, pc, mode):
  return program[program[pc + 2]] if mode == 0 else program[pc + 2]


def run(program: Sequence[int], inputs: list, is_feedback=False, pc=0) -> (int, int):
  program = list(program)
  diagnostic_code = 0
  pc = pc
  while pc < len(program):
    opcode_obj = decode_opcode(program[pc])
    opcode = opcode_obj[3] * 10 + opcode_obj[4]
    op1_mode = opcode_obj[2]
    op2_mode = opcode_obj[1]
    if opcode == 1 or opcode == 2:
      op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
      dest = program[pc + 3]
      program[dest] = op1 + op2 if opcode == 1 else op1 * op2
      pc += 4
    elif opcode == 3:
      if len(inputs) == 0:
        raise Exception('no input.txt.txt!')
      program[program[pc + 1]] = inputs.pop(0)
      pc += 2
    elif opcode == 4:
      op1 = get_op1(program, pc, op1_mode)
      diagnostic_code = op1
      pc += 2
      if is_feedback:
        return diagnostic_code, pc
    elif opcode == 5 or opcode == 6:
      op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
      pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else pc + 3
    elif opcode == 7:
      op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
      program[program[pc + 3]] = 1 if op1 < op2 else 0
      pc += 4
    elif opcode == 8:
      op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
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


def get_phase_permutations(phases: range) -> list:
  phase_perms = [[]]
  for n in phases:
    new_perm = []
    for perm in phase_perms:
      for i in range(len(perm) + 1):
        new_perm.append(perm[:i] + [n] + perm[i:])
        phase_perms = new_perm
  return phase_perms


def part_one(program: str) -> int:
  max_thruster_signal = 0
  program = read_intcode(program)
  phase_perms = get_phase_permutations(range(0, 5))
  for phase_perm in phase_perms:
    output = 0
    while len(phase_perm) > 0:
      output = run(program, [phase_perm.pop(0), output])
    max_thruster_signal = max(max_thruster_signal, output)
  return max_thruster_signal


def run_with_phase_setting(program: Sequence[int], phase_setting: list) -> int:
  programs, pcs, inputs = [], [], []
  num_amps = len(phase_setting)
  amp_output = 0
  for i in range(0, num_amps):
    programs.append(program)
    pcs.append(0)
    inputs.append([phase_setting[i]])
  while pcs[0] is not None:
    for i in range(0, num_amps):
      inputs[i].append(amp_output)
      amp_output, pc = run(programs[i], inputs[i], True, pcs[i])
      pcs[i] = pc
  return inputs[0][0]


def part_two(program: str) -> int:
  max_thruster_signal = 0
  for phase_perm in get_phase_permutations(range(5, 10)):
    max_thruster_signal = max(max_thruster_signal, run_with_phase_setting(read_intcode(program), phase_perm))
  return max_thruster_signal
