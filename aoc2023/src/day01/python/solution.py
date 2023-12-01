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
def _find_first_digit(string: str) -> int:
  """Returns the left-most digit in a string."""
  return next(int(char) for char in string if char.isdigit())


def _find_last_digit(string: str) -> int:
  """Returns the right-most digit in a string."""
  return next(
    int(string[i]) for i in range(len(string) - 1, -1, -1)
    if string[i].isdigit())


def _get_calibration_value(string: str) -> int:
  """Calculates calibration value of a string."""
  return _find_first_digit(string) * 10 + _find_last_digit(string)


def sum_calibration_values(calibration_document: tuple[str, ...]) -> int:
  """Calculates sum of the calibration values.

  The calibration value can be found by combining the first digit and the last
   digit (in that order) to form a single two-digit number.

  Args
    calibration_document A calibration document.
  Returns
    Sum of all calibration values in the document.
  """
  return sum((_get_calibration_value(line) for line in calibration_document))
