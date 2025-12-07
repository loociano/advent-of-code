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


def _has_repeated_sequence_twice(product_id: str) -> bool:
  """Returns true iff a product ID consist of a sequence of digits repeated
  exactly twice."""
  if len(product_id) % 2 != 0:
    return False
  half = len(product_id) // 2
  for i in range(0, half):
    if product_id[i] != product_id[half + i]:
      return False
  return True


def is_valid_id(product_id: str) -> bool:
  """Returns true iff an ID is valid"""
  return not _has_repeated_sequence_twice(product_id)


def find_invalid_ids(id_range: Sequence[int]) -> Sequence[int]:
  """Finds invalid IDs in an ID range.

  For example range(11, 23) returns invalid IDs (11, 22)."""
  return tuple(i for i in id_range if not is_valid_id(product_id=str(i)))


def find_all_invalid_ids(id_ranges: str) -> Sequence[int]:
  """Returns all the invalid IDs given a CSV list of ranges.

  A range is defined as 'start-end', example: '11-22'.
  """
  invalid_ids = []
  for id_range in id_ranges.split(','):
    start, end = id_range.split('-')
    invalid_ids += find_invalid_ids(id_range=range(int(start), int(end) + 1))
  return tuple(invalid_ids)
