# Copyright 2020 Google LLC
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
from math import ceil, floor

from typing import List


def part_one(timestamp: int, bus_ids: List[str]) -> int:
  """
  Args:
    timestamp: example 939
    bus_ids: comma-separated bus ids, x if unavailable. Example 7,13,x,x
  Returns
  ID of the earliest bus that can be taken to the airport multiplied by the
  number of minutes needed to wait for that bus.
  """
  max_wait_since_timestamp = 0
  earliest_bus_id = 0
  for bus_id in bus_ids:
    if bus_id != 'x':
      wait_since_timestamp = (timestamp / int(bus_id)) - (timestamp // int(bus_id))
      if wait_since_timestamp > max_wait_since_timestamp:
        max_wait_since_timestamp = wait_since_timestamp
        earliest_bus_id = int(bus_id)
  departure_timestamp = ceil(timestamp / earliest_bus_id) * earliest_bus_id
  return earliest_bus_id * (departure_timestamp - timestamp)


def part_two(bus_ids: List[str]) -> int:
  """
  Args:
    bus_ids: comma-separated bus ids, x to skip position. Example 7,13,x,x

  Returns:
    Earliest timestamp such that all of the listed bus IDs depart at offsets
    matching their positions in the list.
  """
  step = 1
  while True:
    found = True
    guess = step * int(bus_ids[0])
    for i, bus_id in enumerate(bus_ids):
      if bus_id != 'x':
        b = (guess + i) / int(bus_ids[i])
        if b - floor(b) > 0:
          found = False
          break
    if found:
      return guess
    step += 1