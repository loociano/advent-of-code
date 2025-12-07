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
from typing import Callable, Sequence


def _is_made_of_sequence_exactly_twice(product_id: str) -> bool:
  """Returns true iff a product ID consist of a sequence of digits repeated
  exactly twice."""
  if len(product_id) % 2 != 0:
    return False
  half = len(product_id) // 2
  for i in range(0, half):
    if product_id[i] != product_id[half + i]:
      return False
  return True


def _is_made_of_sequence(product_id: str, sequence_length: int) -> bool:
  """Returns True iff a product IDs is made of a sequence of a given length."""
  for i in range(0, sequence_length):
    for j in range(i, len(product_id), sequence_length):
      if product_id[j] != product_id[i]:
        return False
  return True


def _is_made_of_repeated_sequence_at_least_twice(product_id: str) -> bool:
  """Returns True if a product ID is made only of a sequence repeated at least
  twice"""
  if len(product_id) < 2:
    # Need at least two digits.
    return False
  if len(product_id) % 2 == 0:  # Even length.
    # Even lengths can be 2, 4, 6, 8 or 10.
    if _is_made_of_sequence(product_id=product_id, sequence_length=len(product_id) // 2):
      return True
    if len(product_id) > 4:
      # In these cases try length 2. 6=3x2, 8=2x2x2, 10=5x2.
      return _is_made_of_sequence(product_id=product_id, sequence_length=2)
    return False
  else:  # Odd length.
    # Max input range length is 10, hence max odd length is 9.
    sequence_length = 1 if len(product_id) < 9 else 3  # For length 9 we must try 3-digit sequence.
    return _is_made_of_sequence(product_id=product_id, sequence_length=sequence_length)


def is_valid_id(product_id: str) -> bool:
  """Returns true iff an ID is valid."""
  return not _is_made_of_sequence_exactly_twice(product_id)


def is_valid_id_part2(product_id: str) -> bool:
  """Returns True iff an ID is valid.

  A product ID is invalid if is made only of some sequence of digits repeated
  at least twice.
  """
  return not _is_made_of_repeated_sequence_at_least_twice(product_id)


def find_invalid_ids(id_range: Sequence[int],
                     validation_function: Callable[[str], bool]
                     = is_valid_id) -> Sequence[int]:
  """Finds invalid IDs in an ID range.

  For example range(11, 23) returns invalid IDs (11, 22)."""
  return tuple(i for i in id_range if not validation_function(str(i)))


def find_all_invalid_ids(id_ranges: str,
                         validation_function: Callable[[str], bool]
                         = is_valid_id) -> Sequence[int]:
  """Returns all the invalid IDs given a CSV list of ranges.

  A range is defined as 'start-end', example: '11-22'.
  """
  invalid_ids = []
  for id_range in id_ranges.split(','):
    start, end = id_range.split('-')
    invalid_ids += find_invalid_ids(id_range=range(int(start), int(end) + 1),
                                    validation_function=validation_function)
  return tuple(invalid_ids)
