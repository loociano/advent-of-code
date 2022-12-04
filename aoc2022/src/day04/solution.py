# Copyright 2022 Google LLC
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


def _is_fully_contained(first: str, second: str) -> bool:
  begin1, end1 = map(int, first.split('-'))
  begin2, end2 = map(int, second.split('-'))
  length1 = end1 - begin1 + 1
  length2 = end2 - begin2 + 1
  if length1 > length2:
    # first may contain second.
    if begin2 >= begin1 and end2 <= end1:
      return True
  elif length2 > length1:
    # second may contain first.
    if begin1 >= begin2 and end1 <= end2:
      return True
  return begin1 == begin2 and end1 == end2


def _overlaps(first: str, second: str) -> bool:
  begin1, end1 = map(int, first.split('-'))
  begin2, end2 = map(int, second.split('-'))
  if end1 < begin2 or begin2 > end1 or end2 < begin1 or begin1 > end2:
    return False
  return True


def count_fully_contained_pairs(pairs: Sequence[str]) -> int:
  return sum(
    [1 if _is_fully_contained(*pair.split(',')) else 0 for pair in pairs])


def count_overlapping_pairs(pairs: Sequence[str]) -> int:
  return sum(
    [1 if _overlaps(*pair.split(',')) else 0 for pair in pairs])
