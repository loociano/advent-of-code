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
from functools import cache


def _has_even_num_digits(number: int) -> bool:
  """Returns true if an integer has an even number of digits.
  Examples: 1234 is True and 123 is False."""
  return len(str(number)) % 2 == 0


class Simulation:
  def __init__(self, initial_state: str):
    self._roots = tuple([int(stone) for stone in initial_state.split()])

  @cache
  def _iterate(self, value: int, num_iterations: int = 0) -> int:
    """Returns the number of stones after iteration."""
    if num_iterations == 0:
      return 1  # Leaf node
    if value == 0:
      return self._iterate(1, num_iterations - 1)
    elif _has_even_num_digits(value):
      half_digits = len(str(value)) // 2
      # Break stone into 2:
      return (self._iterate(int(str(value)[:half_digits]), num_iterations - 1)
              + self._iterate(int(str(value)[half_digits:]), num_iterations - 1))
    else:
      return self._iterate(value * 2024, num_iterations - 1)

  def simulate(self, num_iterations=0) -> int:
    """Simulates the rules of stones a given number of times."""
    return sum(self._iterate(root, num_iterations) for root in self._roots)


def count_stones(initial_state: str, blinks: int = 0) -> int:
  """Counts the number of stones after a number of blinks."""
  return Simulation(initial_state).simulate(num_iterations=blinks)
