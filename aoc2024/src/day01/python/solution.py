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
from collections import defaultdict
from typing import Sequence

type LocationIds = Sequence[int]

def _parse_input(input: Sequence[str]) -> tuple[LocationIds, LocationIds]:
  """Converts puzzle input into 2 lists of location IDs.

  n = len(input)
  Time complexity: O(n)
  Space complexity: O(n) + O(n) = O(n)

  """
  location_ids1 = []
  location_ids2 = []
  # Parse input:
  for line in input:  # t:O(n)
    # Line format is: '<int>\s\s\s<int>'
    id1, id2 = map(int, line.split('   ')) # Assumes valid input.
    location_ids1.append(id1)
    location_ids2.append(id2)
  return location_ids1, location_ids2

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
  location_ids1.sort()  # t:O(nlogn)
  location_ids2.sort()  # t:O(nlogn)
  return sum(
    abs(location_ids1[i] - location_ids2[i])
    for i in range(0, len(location_ids1)))  # t:O(n)

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
  histogram = defaultdict(int)
  # Generate histogram:
  for id in location_ids2:  # t:O(n)
    histogram[id] += 1
  # Calculate similarity score:
  return sum(id * histogram.get(id, 0) for id in location_ids1)  # t:O(n)