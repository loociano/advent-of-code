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
from functools import cache


@cache
def _is_possible(design: str, patterns: frozenset[str], candidate: str = '') -> bool:
  """Returns true if the design can be made with the available patterns."""
  for pattern in patterns:
    testee = candidate + pattern
    if testee == design or (design.startswith(testee) and _is_possible(design, patterns, testee)):
      return True
  return False


@cache
def _count_distinct_arrangements(design: str, patterns: frozenset[str], prefix: str, k: int) -> int:
  """Returns the number of distinct arrangements that can be made to create a 'design'
  from available 'patterns'.
  Example: given design 'brwrr' and patterns 'b','r','br','wr',
  it can be made in 2 different ways: b+r+wr+r or br+wr+r."""
  if k == 0:  # Base case
    return 1
  return sum(
    _count_distinct_arrangements(design=design,
                                 patterns=patterns,
                                 prefix=prefix + pattern,
                                 k=k - len(pattern))
    if design.startswith(prefix + pattern)
    else 0
    for pattern in patterns)


def num_possible_designs(input: Sequence[str]) -> int:
  """Returns the total number of designs that can be made with the available patterns."""
  patterns: frozenset[str] = frozenset(input[0].split(', '))  # First line has comma-separated patterns.
  return sum(_is_possible(design, patterns)
             for design in input[2:])  # Designs start on the third line.


def num_possible_options(input: Sequence[str]) -> int:
  """Returns the total number of different ways the designs can be made with the available patterns."""
  patterns: frozenset[str] = frozenset(input[0].split(', '))  # First line has comma-separated patterns.
  return sum(_count_distinct_arrangements(design=design, patterns=patterns, prefix='', k=len(design))
             for design in input[2:])  # Designs start on the third line.
