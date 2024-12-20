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
  for pattern in patterns:
    testee = candidate + pattern
    if testee == design:
      return True
    if design.startswith(testee):
      if _is_possible(design, patterns, testee):
        return True
  return False


def num_possible_designs(input: Sequence[str]) -> int:
  patterns: frozenset[str] = frozenset(input[0].split(', '))
  result = 0
  for design in input[2:]:
    result += 1 if _is_possible(design, patterns) else 0
  return result
