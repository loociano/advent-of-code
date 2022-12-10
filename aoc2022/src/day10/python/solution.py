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

_INSTR_CYCLES = {
  'noop': 1,
  'addx': 2
}

_SIGNAL_STRENGTHS = {
  20: None,
  60: None,
  100: None,
  140: None,
  180: None,
  220: None
}


def _eval_cycle(cycle: int, register_x: int) -> None:
  if cycle in _SIGNAL_STRENGTHS:
    _SIGNAL_STRENGTHS[cycle] = register_x * cycle


def sum_six_signal_strengths(instructions: Sequence[str]) -> int:
  cycle = 0
  register_x = 1
  for instr in instructions:
    if instr == 'noop':
      cycle += 1
      _eval_cycle(cycle, register_x)
    elif instr.startswith('addx'):
      _, amount = instr.split()
      cycle += 1
      _eval_cycle(cycle, register_x)
      cycle += 1
      _eval_cycle(cycle, register_x)
      register_x += int(amount)
    else:
      raise ValueError('Unknown instruction [%s]', instr)
  return sum([strength for strength in _SIGNAL_STRENGTHS.values()])
