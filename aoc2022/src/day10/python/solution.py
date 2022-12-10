# Copyright 2022 Google LLC
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


class CPU:
  def __init__(self, instructions: Sequence[str]) -> None:
    self._instructions = instructions
    self._register_x = 1
    self._cycle = 0
    self._historical_x = {
      20: None,
      60: None,
      100: None,
      140: None,
      180: None,
      220: None
    }

  def _incr_cycle(self) -> None:
    self._cycle += 1
    if self._cycle in self._historical_x:
      self._historical_x[self._cycle] = self._register_x

  def run(self) -> None:
    for instr in self._instructions:
      if instr == 'noop':
        self._incr_cycle()
      elif instr.startswith('addx'):
        _, amount = instr.split()
        self._incr_cycle()
        self._incr_cycle()
        self._register_x += int(amount)
      else:
        raise ValueError('Unknown instruction [%s]', instr)

  def calc_signal_strengths(self) -> int:
    return sum(
      [cycle * register_x for cycle, register_x in self._historical_x.items()])


def sum_six_signal_strengths(instructions: Sequence[str]) -> int:
  cpu = CPU(instructions)
  cpu.run()
  return cpu.calc_signal_strengths()
