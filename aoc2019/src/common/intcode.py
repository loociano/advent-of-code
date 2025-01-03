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


def read_intcode(intcode_program: str) -> Sequence[int]:
  """Parses raw intcode program."""
  return tuple(map(int, intcode_program.split(',')))


class Intcode:

  def __init__(self, program: Sequence[int]):
    self.pc = 0
    self.relative_base = 0
    self.input_val = 0
    self.output = None
    self.stopped_on_input = False
    self.mem = [0] * 100000
    for pos, intcode in enumerate(program):
      self.mem[pos] = intcode

  def set_input(self, input_val: int):
    self.input_val = input_val

  def get_output(self):
    return self.output

  def run_until_input_or_done(self) -> int:
    return self.run(False, True)

  def run_until_io_or_done(self) -> int:
    return self.run(True, True)

  def run(self, stop_on_output=True, stop_on_input=False) -> int or None:
    self.stopped_on_input = False
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
        self.mem[self._get_op3_address(op1_mode, 1)] = self.input_val
        self.pc += 2
        self.stopped_on_input = True
        if stop_on_input:
          break
      elif opcode == 4:
        op1 = self._get_op1(op1_mode)
        self.output = op1
        self.pc += 2
        if stop_on_output:
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
        return
      else:
        print('unknown opcode')
        break
    return self.output

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
