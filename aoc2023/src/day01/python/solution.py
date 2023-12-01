# Copyright 2023 Google LLC
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
_SPELLED_OUT_NUMBERS = (
  'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
_NUMBERS = tuple(str(i) for i in range(0, 10))


def _find_first_digit(string: str, read_spelled: bool) -> int:
  """Returns the left-most digit in a string."""
  if not read_spelled:
    return next(int(char) for char in string if char.isdigit())

  min_index = len(string)
  found_index = len(string)
  num_at_min_index = None
  for number in _NUMBERS:
    try:
      found_index = string.index(number)
    except ValueError:
      # Number not found, ignore.
      pass
    if found_index < min_index:
      num_at_min_index = int(number)
      min_index = found_index
  for i in range(len(_SPELLED_OUT_NUMBERS)):
    try:
      found_index = string.index(_SPELLED_OUT_NUMBERS[i])
    except ValueError:
      # Number not found, ignore.
      pass
    if found_index < min_index:
      num_at_min_index = int(i)
      min_index = found_index
  return num_at_min_index


def _find_last_digit(string: str, read_spelled: bool) -> int:
  """Returns the right-most digit in a string."""
  if not read_spelled:
    return next(
      int(string[i]) for i in range(len(string) - 1, -1, -1)
      if string[i].isdigit())

  max_index = -1
  found_index = -1
  num_at_max_index = None
  for number in _NUMBERS:
    try:
      found_index = string.rfind(number)
    except ValueError:
      # Number not found, ignore.
      pass
    if found_index > max_index:
      num_at_max_index = int(number)
      max_index = found_index
  for i in range(len(_SPELLED_OUT_NUMBERS)):
    try:
      found_index = string.rfind(_SPELLED_OUT_NUMBERS[i])
    except ValueError:
      # Number not found, ignore.
      pass
    if found_index > max_index:
      num_at_max_index = int(i)
      max_index = found_index
  return num_at_max_index


def _get_calibration_value(string: str,
                           read_spelled: bool) -> int:
  """Calculates calibration value of a string."""

  return (_find_first_digit(string, read_spelled) * 10
          + _find_last_digit(string, read_spelled))


def sum_calibration_values(calibration_document: tuple[str, ...],
                           read_spelled: bool = False) -> int:
  """Calculates sum of the calibration values.

  The calibration value can be found by combining the first digit and the last
   digit (in that order) to form a single two-digit number.

  Args
    calibration_document A calibration document.
    read_spelled Whether to consider spelled out numbers in the calibration
        document lines. False by default.
  Returns
    Sum of all calibration values in the document.
  """
  return sum(
    (_get_calibration_value(line, read_spelled)
     for line in calibration_document))
