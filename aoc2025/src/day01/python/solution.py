# Copyright 2025 Google LLC
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
import re


class Dial:
  _NUM_POSITIONS = 100

  def __init__(self, start_position: int = 50):
    """Creates a dial. A dial has a position that ranges from 0 to 99.

    Args:
      start_position: 50 by default.
    """
    if not (0 <= start_position < self._NUM_POSITIONS):
      raise ValueError(f'Start position must be between 0 and 99, was: {start_position}')
    self.position = start_position

  def rotate(self, num_rotations: int) -> None:
    """Rotates the dial by a number of rotations and returns the number of
    times it crosses zero.

    Rotations can be positive (rotate right) or negative (rotate left).
    """
    new_position = self.position + num_rotations
    while new_position < 0:
      new_position += self._NUM_POSITIONS
    while new_position >= self._NUM_POSITIONS:
      new_position -= self._NUM_POSITIONS
    self.position = new_position


def find_password(rotations: Sequence[str]) -> int:
  """Returns the number of times the dial is left pointing at 0 after any
  rotation in the sequence"""
  dial = Dial()
  count_position_zero = 0
  for rotation in rotations:
    matches = re.match(r'(?P<direction>[LR])(?P<num_rotations>\d+)', rotation)
    if matches is None:
      raise ValueError(f'Invalid rotation {rotation}, expected format [LR]\d+')
    direction = matches.groupdict()['direction']
    num_rotations = matches.groupdict()['num_rotations']
    dial.rotate(num_rotations=int(num_rotations) * (-1 if direction == 'L' else 1))
    count_position_zero += 1 if dial.position == 0 else 0
  return count_position_zero
