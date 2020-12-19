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
from typing import List, Dict, Tuple


def part_one(starting_numbers: List[int], stop=2020) -> int:
  """
  Returns:
    The 2020th number spoken.
  """
  return _play_memory_game(starting_numbers, stop)


def part_two(starting_numbers: List[int], stop: int) -> int:
  """
  Returns:
    The 30000000th number spoken.
  """
  return _play_memory_game(starting_numbers, stop)


def _play_memory_game(starting_numbers: List[int], stop=2020) -> int:
  """
  Plays memory game until stop.
  Args:
    starting_numbers
    stop
  Returns
    nth spoken number.
  """
  mem = [0] * stop  # records last turn a given number was spoken, 0 otherwise.
  for turn in range(len(starting_numbers) - 1):
    mem[starting_numbers[turn]] = turn + 1
  turn = len(starting_numbers)
  last_spoken = starting_numbers[-1:][0]

  while turn <= stop:
    if mem[last_spoken] == 0:  # first time it was spoken
      next_spoken = 0
    else:
      next_spoken = turn - mem[last_spoken]
    mem[last_spoken] = turn
    last_spoken = next_spoken
    turn += 1
  return mem.index(stop)