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
from typing import Callable, Sequence
from itertools import product

_OPERATORS: dict[str, Callable] = {
  '+': lambda a, b: a + b,
  '*': lambda a, b: a * b,
  '||': lambda a, b: int(str(a) + str(b))
}


def _could_be_true(equation_data: str, operators: tuple[str, ...]) -> int | None:
  """Returns equation result if it can be made true with some combination of addition and multiplication."""
  result, operands = equation_data.split(': ')
  result = int(result)
  operands = operands.split()
  combinations = list(product(operators, repeat=len(operands) - 1))
  for combination in combinations:
    operands_queue = list(map(int, operands))
    operators_queue = list(combination)
    computation = operands_queue.pop(0)
    while len(operands_queue):
      # Cannot use eval() because it follows math precedence rules.
      computation = _OPERATORS.get(operators_queue.pop(0))(computation, operands_queue.pop(0))
      if computation > result:
        break  # All operands increase computation so we can leave early.
    if computation == result:
      return result
  return None


def calc_calibration(
        equations: Sequence[str],
        operators: tuple[str, ...] = ('+', '*')) -> int:
  """Returns the total calibration result, which is the sum of the equations that
  can be made true with some combination of operators."""
  total_calibration = 0
  for equation_data in equations:
    result = _could_be_true(equation_data, operators)
    if result is not None:
      total_calibration += result
  return total_calibration
