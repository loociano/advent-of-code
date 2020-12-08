# Copyright 2020 Google LLC
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
from typing import List


class Instruction:
  def __init__(self, opcode: str, param: int):
    self.opcode = opcode
    self.param = param

class Computer:
  def __init__(self, boot_code: List[str]) -> None:
    self._instructions = self._boot_code_to_instructions(boot_code)
    self._pc = 0
    self._acc = 0

  def run_until_repeat_instruction(self) -> int:
    """Runs until an instruction is about to run a second time.
    Returns:
      Value of the accumulator before running a instruction a second time.
    """
    visited = [False] * len(self._instructions)
    while self._pc < len(self._instructions):
      if visited[self._pc]:
        return self._acc
      visited[self._pc] = True
      self._execute()
    # Program terminated.
    raise Exception(self._acc)

  def _execute(self):
    """Executes one instruction."""
    instr = self._instructions[self._pc]
    if instr.opcode == 'nop':
      self._pc += 1
    elif instr.opcode == 'acc':
      self._acc += instr.param
      self._pc += 1
    elif instr.opcode == 'jmp':
      self._pc += instr.param
    else:
      raise Exception('Unknown opcode: {}'.format(instr.opcode))

  @staticmethod
  def _boot_code_to_instructions(boot_code: List[str]) -> List[Instruction]:
    instructions = []
    for line in boot_code:
      opcode, str_param = line.split(' ')
      instructions.append(Instruction(opcode, int(str_param)))
    return instructions


def part_one(boot_code: List[str]) -> int:
  """Runs boot code.
  Args:
    boot_code: program
  Returns:
    Value of accumulator before any instruction is executed a second time.
  """
  return Computer(boot_code).run_until_repeat_instruction()


def part_two(boot_code: List[str]) -> int:
  """Fixes a corrupted nop or jmp instruction to make the program terminate.
  Args:
    boot_code: program
  Returns:
    Value of the accumulator after the fixed program terminated.
  """
  for line_num, line in enumerate(boot_code):
    if 'nop' in line:
      copy = boot_code.copy()
      copy[line_num] = line.replace('nop', 'jmp')  # Attempt to fix.
      try:
        Computer(copy).run_until_repeat_instruction()
      except Exception as e:
        return int(str(e))
    if 'jmp' in line:
      copy = boot_code.copy()
      copy[line_num] = line.replace('jmp', 'nop')  # Attempt to fix.
      try:
        Computer(copy).run_until_repeat_instruction()
      except Exception as e:
        return int(str(e))
  raise Exception('Could not fix corrupted instruction.')
