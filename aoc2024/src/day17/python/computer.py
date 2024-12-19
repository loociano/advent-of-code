# Copyright 2024 Google LLC
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
from typing import Sequence, Callable, Tuple

type Instr = tuple[Callable, Callable]


def _get_literal_value(literal_operand) -> int:
  if literal_operand < 0 or literal_operand > 7:
    raise ValueError(f'Unsupported literal operand: {literal_operand}')
  return literal_operand


class Computer:

  def __init__(self, program: Sequence[int], reg_a: int = 0, reg_b: int = 0, reg_c: int = 0) -> None:
    self._program = program
    self.reg_a: int = reg_a
    self.reg_b: int = reg_b
    self.reg_c: int = reg_c
    self._instr_pointer: int = 0
    self._instr_set: list[Instr] = [
      (self._adv, self._get_combo_value),
      (self._bxl, _get_literal_value),
      (self._bst, self._get_combo_value),
      (self._jnz, _get_literal_value),
      (self._bxc, _get_literal_value),
      (self._out, self._get_combo_value),
      (self._bdv, self._get_combo_value),
      (self._cdv, self._get_combo_value),
    ]
    self._stdout: list[int] = []

  def execute(self) -> None:
    """Executes the program then halts."""
    while not self.is_halted():
      self._execute_next_instr()

  def stdout(self) -> tuple[int, ...]:
    return tuple(self._stdout)

  def is_halted(self) -> bool:
    return self._instr_pointer > len(self._program) - 2

  def _execute_next_instr(self) -> None:
    next_instr = self._instr_set[self._program[self._instr_pointer]]
    executable = next_instr[0]
    operand = next_instr[1](self._program[self._instr_pointer + 1])
    executable(operand)
    self._instr_pointer += 2

  def flush(self) -> str:
    """Flushes the buffered stdout."""
    return ','.join(map(str, self._stdout))

  def _get_combo_value(self, combo_operand: int) -> int:
    if 0 <= combo_operand <= 3:
      return combo_operand
    if combo_operand == 4:
      return self.reg_a
    if combo_operand == 5:
      return self.reg_b
    if combo_operand == 6:
      return self.reg_c
    raise ValueError(f'Unsupported combo operand: {combo_operand}')

  def _adv(self, operand: int) -> None:
    """Updates register A with the result of dividing register A by 2^combo_operand."""
    self.reg_a = self._divide(operand)

  def _divide(self, operand: int) -> int:
    return self.reg_a >> operand

  def _bxl(self, operand: int) -> None:
    """Updates register B with bitwise XOR of register B and operand."""
    self.reg_b ^= operand

  def _bst(self, operand: int) -> None:
    """Updates register B with operand modulo 8."""
    self.reg_b = operand % 8

  def _jnz(self, operand: int) -> None:
    """Jumps to given address if register A is zero, otherwise NOP."""
    if self.reg_a == 0:
      return
    self._instr_pointer = operand - 2  # Compensate the instr pointer update.

  def _bxc(self, operand: int) -> None:
    """Updates register B with B XOR C."""
    del operand  # Ignore.
    self.reg_b ^= self.reg_c

  def _out(self, operand: int) -> None:
    """Outputs the combo operand modulo 8."""
    self._stdout.append(operand % 8)

  def _bdv(self, operand: int) -> None:
    """Updates register B with the result of dividing register A by 2^combo_operand."""
    self.reg_b = self._divide(operand)

  def _cdv(self, operand: int) -> None:
    """Updates register C with the result of dividing register A by 2^combo_operand."""
    self.reg_c = self._divide(operand)
