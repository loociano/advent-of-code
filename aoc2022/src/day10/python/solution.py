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

_SCREEN_WIDTH = 40
_SCREEN_HEIGHT = 6


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
    self._screen = []
    for _ in range(0, _SCREEN_HEIGHT):
      self._screen.append([''] * _SCREEN_WIDTH)
    self._screen_y_pos = -1

  def _incr_cycle(self) -> None:
    self._cycle += 1
    if self._cycle in self._historical_x:
      self._historical_x[self._cycle] = self._register_x
    # Draw screen pixel.
    if (self._cycle - 1) % _SCREEN_WIDTH == 0:
      self._screen_y_pos += 1
    screen_x_pos = (self._cycle - 1) % _SCREEN_WIDTH
    pixel_has_sprite = (
        screen_x_pos == self._register_x - 1
        or screen_x_pos == self._register_x
        or screen_x_pos == self._register_x + 1)
    self._screen[self._screen_y_pos][
      screen_x_pos] = '#' if pixel_has_sprite else '.'

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

  def get_screen(self) -> str:
    return '\n'.join(
      [''.join(self._screen[line]) for line in range(len(self._screen))])

  def calc_signal_strengths(self) -> int:
    return sum(
      [cycle * register_x for cycle, register_x in self._historical_x.items()])


def sum_six_signal_strengths(instructions: Sequence[str]) -> int:
  cpu = CPU(instructions)
  cpu.run()
  return cpu.calc_signal_strengths()


def show_screen(instructions: Sequence[str]) -> str:
  cpu = CPU(instructions)
  cpu.run()
  return cpu.get_screen()
