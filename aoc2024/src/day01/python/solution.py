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
from collections import Counter
from typing import Sequence, TypeAlias

_LocationIds: TypeAlias = Sequence[int]

def _parse_input(input: Sequence[str]) -> tuple[_LocationIds, _LocationIds]:
  """Converts puzzle input into 2 sequences of location IDs.

  n = len(input)
  Time complexity: O(n)
  Space complexity: O(n) + O(n) = O(n)

  """
  location_ids1 = []
  location_ids2 = []
  # Parse input:
  for line in input:  # t:O(n)
    # Line format is: '<int>\s\s\s<int>'
    id1, id2 = map(int, line.split())
    location_ids1.append(id1)
    location_ids2.append(id2)
  return tuple(location_ids1), tuple(location_ids2)

def calculate_distance(input: Sequence[str]) -> int:
  """
  Calculates total distance between 2 sequences of location IDs.

  n = len(input)
  Time complexity: O(n) + O(2nlogn) + O(n) = O(nlogn).
  Space complexity: O(n) + O(n) = O(n)

  Args:
    input: Sequence of location ID pairs.
  Returns
    Total distance.
  """
  location_ids1, location_ids2 = _parse_input(input)  # O(n)
  # Calculate total distance:
  sorted_ids1, sorted_ids2 = sorted(location_ids1), sorted(location_ids2)  # t: O(2nlogn)
  return sum(
    abs(id1 - id2)
    for id1, id2 in zip(sorted_ids1, sorted_ids2))  # t:O(n)

def calculate_similarity_score(input: Sequence[str]) -> int:
  """
  Calculates similarity score between 2 sequences of location IDs.

  n = len(input)
  Time complexity: O(n) + O(n) + O(n) = O(n)
  Space complexity: O(2n) + O(n) = O(n)

  Args:
    input: Sequence of location ID pairs.
  Returns
    Total distance.
  """
  location_ids1, location_ids2 = _parse_input(input)  # t:O(n)
  counter = Counter(location_ids2)
  # Calculate similarity score:
  return sum(id * counter.get(id, 0) for id in location_ids1)  # t:O(n)