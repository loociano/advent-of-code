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


def _get_item_pos(item: str) -> int:
  if ord('a') <= ord(item) <= ord('z'):
    return ord(item) - ord('a')
  elif ord('A') <= ord(item) <= ord('Z'):
    return ord(item) - ord('A') + 26
  raise ValueError('Item is not [a-zA-Z], was %s', item)


def _calculate_priorities(rucksack: str) -> int:
  items = [0] * 52  # a-z + A-Z
  compartment_length = len(rucksack) // 2

  # First compartment.
  for i in range(0, compartment_length):
    items[_get_item_pos(rucksack[i])] = 1
  # Second compartment.
  for i in range(compartment_length, len(rucksack)):
    item_pos = _get_item_pos(rucksack[i])
    if items[item_pos] == 1:
      return item_pos + 1  # Item priority.
  raise ValueError('Did not find a repeated item.')


def sum_priorities_common_types(rucksacks: Sequence[str]) -> int:
  return sum([_calculate_priorities(r) for r in rucksacks])
