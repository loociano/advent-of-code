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
from math import prod
from enum import Enum
from typing import Callable, Sequence
from dataclasses import dataclass, field


class _Operator(Enum):
  """Supported operators."""
  UNKNOWN = 1
  PRODUCT = 2
  ADD = 3


@dataclass
class _Problem:
  """Represents a problem to compute."""
  operator: _Operator = _Operator.UNKNOWN
  operands: list[int] = field(default_factory=list)

  def compute(self) -> int:
    if self.operator == _Operator.PRODUCT:
      return prod(self.operands)
    if self.operator == _Operator.ADD:
      return sum(self.operands)
    raise ValueError('Problem has no supported operator!')


def _parse_lines(lines: Sequence[str]) -> Sequence[_Problem]:
  """Converts input lines into problems."""
  problems = tuple(_Problem() for _ in lines[0].split())
  for i in range(0, len(lines)):
    curr = lines[i]
    tokens = curr.split()
    for j in range(0, len(tokens)):
      problem: _Problem = problems[j]
      token = tokens[j]
      if i == len(lines) - 1:
        if token == '+':
          problem.operator = _Operator.ADD
        elif token == '*':
          problem.operator = _Operator.PRODUCT
        else:
          raise ValueError(f'Unrecognized operator: {token}')
      else:
        problem.operands.append(int(token))
  return problems


def parse_lines2(lines: Sequence[str]) -> Sequence[_Problem]:
  """Reads operands as columns."""
  last_line = lines[-1]
  problems = []
  for i in range(0, len(lines[0])):
    str_operand = ''.join(lines[j][i] for j in range(0, len(lines) - 1))
    if last_line[i] == '*' or last_line[i] == '+':
      # New problem starts
      op = _Operator.PRODUCT if last_line[i] == '*' else _Operator.ADD
      problem = _Problem(operator=op)
      problem.operands.append(int(str_operand))
      problems.append(problem)
    elif not str_operand.isspace():  # Ignore whitespace column.
      last_problem: _Problem = problems[-1]
      last_problem.operands.append(int(str_operand))
  return problems


def calculate_grand_total(lines: Sequence[str], parse_fn: Callable[
  [Sequence[str]], Sequence[_Problem]] = _parse_lines) -> int:
  """Returns the sum of all computed problems given an input and parsing function."""
  return sum(problem.compute() for problem in parse_fn(lines))
