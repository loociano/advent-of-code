# Copyright 2024 Google LLC
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

# A report has a variable number of levels, represented by integers.
type Report = tuple[int, ...]


def _parse_input(input: Sequence[str]) -> Sequence[Report]:
  """Converts puzzle input into a sequence of reports.

  n=len(input), k=len(report)
  Time complexity: O(kn)
  Space complexity: O(kn)
  """
  return tuple(tuple(int(level) for level in line.split()) for line in input)


def _is_inc_or_dec(report: Report) -> bool:
  last = None
  last_sign = None
  for curr in report:
    if last is not None:
      if last == curr:
        return False
      curr_sign = curr - last > 0
      if last_sign is not None:
        if curr_sign != last_sign:
          return False
      last_sign = curr_sign
    last = curr
  return True


def _are_adj_diff_safe(report: Report, safety_range=(1, 3)) -> bool:
  last = None
  for curr in report:
    if last is not None:
      diff = abs(last - curr)
      if diff < safety_range[0] or diff > safety_range[1]:
        return False
    last = curr
  return True


def _could_be_safe(report: Report) -> bool:
  """Returns true if a report could be safe by removing one level."""
  for i in range(len(report)):
    # Drop element and test report safety.
    test_report = report[:i] + report[i + 1:]
    if _is_inc_or_dec(test_report) and _are_adj_diff_safe(test_report):
      return True
  return False


def _is_safe(report: Report, tolerate_bad_level) -> bool:
  """Returns true if a report is safe.

  A report is safe the two conditions are true:
  a) The levels are either all increasing or all decreasing.
  b) Any two adjacent levels differ by at least one and at most three.
  """
  is_safe = _is_inc_or_dec(report) and _are_adj_diff_safe(report)
  if not is_safe and tolerate_bad_level:
    return _could_be_safe(report)
  return is_safe


def num_safe_reports(input: Sequence[str], tolerate_bad_level=False) -> int:
  """Returns the number of safe reports.

  n=len(input), k=len(report)
  Time complexity: O(3k^2n) = O(k^2n)
  Space complexity: O(n+k)
  """
  return sum(_is_safe(report, tolerate_bad_level) for report in _parse_input(input))
