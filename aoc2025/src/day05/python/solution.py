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
  """Returns True if a number is within any interval."""
  for interval in intervals:
    if number in interval:
      return True
  return False


def _parse_lines(lines: Sequence[str]) -> tuple[Sequence[range], Sequence[int]]:
  """Parses input lines into intervals and ingredient IDs."""
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


def _merge_intervals(intervals: Sequence[range]) -> Sequence[range]:
  """Merges intervals.

  [3-6),[10-15),[12-19),[16-21) becomes [3-6),[10,21).
  """
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  merged = [sorted_intervals[0]]
  for i in range(1, len(sorted_intervals)):
    next_interval = sorted_intervals[i]
    last_interval = merged[-1]
    if next_interval[0] > last_interval[-1]:
      # Next interval is disjointed from last one.
      merged.append(next_interval)
    elif next_interval[0] <= last_interval[-1] < next_interval[-1]:
      # Next interval is within last one. Extend last interval accordingly.
      merged[-1] = range(merged[-1][0], next_interval[-1] + 1)
  return tuple(merged)


def count_fresh_ingredients(lines: Sequence[str]) -> int:
  """Counts fresh ingredient IDs given fresh ranges."""
  intervals, numbers = _parse_lines(lines)
  return sum(1 if _is_in_range(intervals=intervals, number=number) else 0
             for number in numbers)


def count_fresh_ingredients_in_range(lines: Sequence[str]) -> int:
  """Counts fresh ingredients considering all ranges."""
  intervals, _ = _parse_lines(lines)
  return sum(len(interval) for interval in _merge_intervals(intervals))
