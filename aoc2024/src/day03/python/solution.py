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
import re
from functools import reduce
from typing import Sequence


def _to_muls(matches: Sequence[str]) -> Sequence[tuple[int, ...]]:
  # Ignore match[0] which contains the raw pair ('1','2') if mul(1,2).
  # match[1] and match[2] capture the individual digits in pair (as string).
  return tuple(tuple(map(int, (match[1], match[2]))) for match in matches)  # t:O(n)


def _calculate(muls: Sequence[tuple[int, ...]]) -> int:
  return sum(reduce(lambda a, b: a * b, mul) for mul in muls)  # t:O(n)


def _find_muls(string: str) -> Sequence[str]:
  return re.findall(r'mul\(((\d+),(\d+))\)', string)  # t:O(n)


def calculate(input: str) -> int:
  """
  Sums all the valid multiplications.
  Example valid multiplications: 'mul(1,2)', 'mul(123,456)'
  """
  matches = _find_muls(input)
  if matches is None:
    raise ValueError('No multiplications were found.')
  return _calculate(_to_muls(matches))


def calculate2(input: str) -> int:
  """
  Sums all valid multiplications between do() and don't() operations.

  At the beginning of the program, mul instructions are enabled.
  Example: mul(1,1)do()mul(2,2)don't() -> 1*1+2*2=5
  """
  # Assumption: do() does not appear before don't(). Verified on my puzzle input.
  result = 0
  first_dont_pos = input.find('don\'t()')
  result += calculate(input[:first_dont_pos])

  sub_input = input[first_dont_pos + len('don\'t()'):]  # Trim beginning.
  while sub_input.find('do()') != -1:
    sub_input = sub_input[sub_input.find('do()'):]  # Trim anything before first do().
    dont_pos = sub_input.find('don\'t()')  # Find the next don't().
    result += calculate(sub_input[:dont_pos])  # Calculate muls between do() and don't()
    sub_input = sub_input[dont_pos + len('don\'t()'):]  # Trim anything before don't()
  # Assumption: last operation is don't(). Verified on my puzzle input.
  return result
