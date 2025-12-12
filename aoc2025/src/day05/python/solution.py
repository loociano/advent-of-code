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


def _is_in_range(intervals: Sequence[range], number: int) -> bool:
  for interval in intervals:
    if number in interval:
      return True
  return False


def _parse_lines(lines: Sequence[str]) -> tuple[Sequence[range], Sequence[int]]:
  intervals = []
  numbers = []
  reading_intervals = True
  for line in lines:
    if line == '':
      reading_intervals = False
      continue
    if reading_intervals:
      begin, end = line.split('-')
      intervals.append(range(int(begin), int(end) + 1))
    else:
      numbers.append(int(line))
  return tuple(intervals), tuple(numbers)


def count_fresh_ingredients(lines: Sequence[str]) -> int:
  intervals, numbers = _parse_lines(lines)
  return sum(1 if _is_in_range(intervals=intervals, number=number) else 0
             for number in numbers)
