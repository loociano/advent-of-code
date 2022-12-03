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
from typing import List, Sequence, Set


def _get_item_pos(item: str) -> int:
  if 'a' <= item <= 'z':
    return ord(item) - ord('a')
  elif 'A' <= item <= 'Z':
    return ord(item) - ord('A') + (ord('z') - ord('a') + 1)
  raise ValueError('Item is not [a-zA-Z], was %s', item)


def _calculate_priorities(rucksack: str) -> int:
  items = [False] * 52  # a-z + A-Z
  compartment_length = len(rucksack) // 2
  # First compartment.
  for i in range(0, compartment_length):
    items[_get_item_pos(rucksack[i])] = True
  # Second compartment.
  for i in range(compartment_length, len(rucksack)):
    item_pos = _get_item_pos(rucksack[i])
    if items[item_pos]:
      return item_pos + 1  # Item priority.
  raise ValueError('Did not find a repeated item.')


def _find_common_item_priority(sets: List[Set]) -> int:
  result = sets[0].intersection(sets[1])
  result = result.intersection(sets[2])
  return _get_item_pos(list(result).pop()) + 1


def sum_priorities_common_types(rucksacks: Sequence[str]) -> int:
  return sum([_calculate_priorities(r) for r in rucksacks])


def sum_priorities_by_group(rucksacks: Sequence[str]) -> int:
  priorities = 0
  elf_ordinal = 0
  group_size = 3
  sets = [set()] * group_size
  for rucksack in rucksacks:
    if elf_ordinal == group_size:
      priorities += _find_common_item_priority(sets)
      elf_ordinal = 0
    sets[elf_ordinal] = set(rucksack)
    elf_ordinal += 1
  # Last rucksack.
  priorities += _find_common_item_priority(sets)
  return priorities
