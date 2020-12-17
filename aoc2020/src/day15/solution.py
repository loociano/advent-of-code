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
from typing import List, Dict


def part_one(starting_numbers: List[int], stop=2020) -> int:
  """
  Returns:
    The 2020th number spoken.
  """
  turn = 1
  last_spoken = None
  mem = {}
  while turn <= stop:
    if turn <= len(starting_numbers):
      last_spoken = starting_numbers[turn - 1]
      _cache(mem, turn, last_spoken)
    else:
      if len(mem.get(last_spoken)) == 1:  # first time it was spoken
        last_spoken = 0
        _cache(mem, turn, last_spoken)
      else:
        turns_spoken = mem.get(last_spoken)
        last_spoken = turns_spoken[-1:][0] - turns_spoken[-2:-1][0]
        _cache(mem, turn, last_spoken)
    print('turn {}: {}'.format(turn, last_spoken))
    turn += 1
  return last_spoken


def _cache(mem: Dict[int, List[int]], turn: int, last_spoken: int) -> None:
  if mem.get(last_spoken) is None:
    mem[last_spoken] = []
  mem[last_spoken].append(turn)