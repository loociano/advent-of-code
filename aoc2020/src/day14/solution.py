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
from math import ceil, floor

from typing import List


def part_one(program: List[str]) -> int:
  """
  Returns:
    Sum of all values left in memory after it completes.
  """
  mask = None
  mem = {}
  for line in program:
    if 'mask' in line:
      mask = line.split('mask = ')[1]
    else:  # write into memory
      dest, value = line.split(' = ')
      mem[dest] = apply_mask(mask, int(value))
  return sum(mem.values())


def apply_mask(mask: str, value: int) -> int:
  result = value
  for i, mask_value in enumerate(mask):
    pos = len(mask) - i - 1
    if mask_value == '0' and (value & (1 << pos)) >> pos == 1:
      result -= 1 << pos  # Overwrite
    elif mask_value == '1' and (value & (1 << pos)) >> pos == 0:
      result += 1 << pos  # Overwrite
  return result





def part_two() -> None:
  return None
