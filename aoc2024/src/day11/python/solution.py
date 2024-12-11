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

class Stone:
  def __init__(self, value: int, next_stone=None):
    self.value: int = value
    self.next: Stone | None = next_stone


class Simulation:
  def __init__(self, initial_state: str):
    self._first_stone = self._parse(initial_state)

  def _parse(self, initial_state: str) -> Stone:
    stones = initial_state.split()
    first = Stone(value=int(stones[0]))
    prev = first
    for i in range(1, len(stones)):
      curr = Stone(value=int(stones[i]))
      prev.next = curr
      prev = curr
    return first

  def blink(self):
    curr = self._first_stone
    while curr is not None:
      if curr.value == 0:
        curr.value = 1
      elif len(str(curr.value)) % 2 == 0:  # Even num of digits:
        half_digits = len(str(curr.value)) // 2
        # Break stone into 2:
        first_value = str(curr.value)[:half_digits]
        second_value = str(curr.value)[half_digits:]
        second_stone = Stone(value=int(second_value), next_stone=curr.next)
        curr.value = int(first_value)
        curr.next = second_stone
        curr = second_stone  # Careful, should not handle the second stone.
      else:
        curr.value *= 2024
      curr = curr.next

  def count_stones(self) -> int:
    # Traverse stones from first.
    num_stones = 0
    curr = self._first_stone
    while curr is not None:
      num_stones += 1
      curr = curr.next
    return num_stones


def count_stones(initial_state: str, blinks: int = 0) -> int:
  simulation = Simulation(initial_state)
  for _ in range(blinks):
    simulation.blink()
  return simulation.count_stones()
