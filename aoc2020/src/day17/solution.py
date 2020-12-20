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
from copy import deepcopy


def part_one(initial_state: List[List[str]], num_cycles=6) -> int:
  """
  Returns:
    Number of cubes in the active state after the number of cycles.
  """
  # if start grid is 3x3, default universe is 15x15
  length = len(initial_state) + (2 * num_cycles)
  universe = _populate_universe(initial_state, num_cycles, length)
  _print_universe(universe, length)
  for cycle in range(num_cycles):
    universe = _simulate(universe, length)
    print('After {} cycle(s):'.format(cycle + 1))
    _print_universe(universe, length)
  return _count_active_cubes(universe, length)


def part_two(initial_state: List[List[str]], num_cycles=6) -> int:
  """
  Returns:
    Number of cubes in the active state after the number of cycles.
  """
  return -1


def _populate_universe(initial_state: List[List[str]], num_cycles: int,
                       length: int) -> Dict[Tuple[int, int, int], str]:
  universe = _build_universe(length)
  for row in range(len(initial_state)):
    for col in range(len(initial_state[row])):
      universe[num_cycles + row, num_cycles + col, 0] = initial_state[row][col]
  return universe


def _build_universe(length: int) -> Dict[Tuple[int, int, int], str]:
  diameter = length // 2
  universe = {}
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        universe[x, y, z] = '.'  # Fill with inactive cubes
  return universe


def _simulate(universe: Dict[Tuple[int, int, int], str],
              length: int) -> Dict[Tuple[int, int, int], str]:
  after = deepcopy(universe)
  diameter = length // 2
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        num_active_neighbours = \
          _count_active_neighbours(universe, length, (x, y, z))
        if universe[x, y, z] == '#' and \
            not (num_active_neighbours == 2 or num_active_neighbours == 3):
          after[x, y, z] = '.'  # converts to inactive
        elif universe[x, y, z] == '.' and num_active_neighbours == 3:
          after[x, y, z] = '#'  # converts to active
  return after


def _count_active_neighbours(universe: Dict[Tuple[int, int, int], str],
                             length: int, pos: Tuple[int, int, int]) -> int:
  num_active_neighbours = 0
  diameter = length // 2
  for x in range(pos[0] - 1, pos[0] + 2):
    for y in range(pos[1] - 1, pos[1] + 2):
      for z in range(pos[2] - 1, pos[2] + 2):
        if x == pos[0] and y == pos[1] and z == pos[2]:
          continue
        if x < 0 or x >= length:
          continue
        if y < 0 or y >= length:
          continue
        if z < -diameter or z > diameter:
          continue
        num_active_neighbours += 1 if universe[x, y, z] == '#' else 0
  return num_active_neighbours


def _count_active_cubes(universe: Dict[Tuple[int, int, int], str],
                        length: int) -> int:
  num_active_cubes = 0
  diameter = length // 2
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        num_active_cubes += 1 if universe[x, y, z] == '#' else 0
  return num_active_cubes


def _print_universe(universe: Dict[Tuple[int, int, int], str],
                    length: int) -> None:
  diameter = length // 2
  for z in range(-diameter, diameter + 1):
    _print_layer_z(universe, z, length)


def _print_layer_z(universe: Dict, z: int, length: int) -> None:
  print('z={}'.format(z))
  for x in range(length):
    line = []
    for y in range(length):
      line.append(universe[x, y, z])
    print(''.join(line))
  print('')