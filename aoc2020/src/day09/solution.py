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


def is_valid_xmas(preamble: List[int], target: int) -> bool:
  for i, val_i in enumerate(preamble):
    for j, val_j in enumerate(preamble):
      if i == j:
        continue
      if val_i + val_j == target:
        return True
  return False


def part_one(preamble_size: int, xmas_data: List[int]) -> int:
  for i in range(preamble_size, len(xmas_data)):
    if not is_valid_xmas(xmas_data[i - preamble_size:i], xmas_data[i]):
      return xmas_data[i]
  raise Exception('Could not find solution.')


def part_two(preamble_size: int, xmas_data: List[int]) -> int:
  invalid_number = part_one(preamble_size, xmas_data)
  for i in range(0, len(xmas_data)):
    running_sum = xmas_data[i]
    min_value = running_sum
    max_value = running_sum
    for j in range(i + 1, len(xmas_data)):
      running_sum += xmas_data[j]
      if xmas_data[j] < min_value:
        min_value = xmas_data[j]
      if xmas_data[j] > max_value:
        max_value = xmas_data[j]
      if running_sum > invalid_number:
        break
      elif running_sum == invalid_number:
        return min_value + max_value
  raise Exception('Did not find solution.')