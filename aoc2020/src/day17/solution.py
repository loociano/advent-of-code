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


def part_one(initial_state: List[List[str]]) -> int:
  """
  Returns:
    Number of cubes in the active state after the number of cycles.
  """
  return _active_cubes_after_simulation(initial_state)


def part_two(initial_state: List[List[str]]) -> int:
  """
  Returns:
    Number of cubes in the active state after the number of cycles.
  """
  return _active_cubes_after_simulation(initial_state, dims=4)


def _active_cubes_after_simulation(initial_state: List[List[str]],
                                   num_cycles=6, dims=3) -> int:
  # if start grid is 3x3, default universe is 15x15
  length = len(initial_state) + (2 * num_cycles)
  universe = _populate_universe(initial_state, num_cycles, length, dims)
  for cycle in range(num_cycles):
    universe = _simulate(universe, length, dims)
  return _count_active_cubes(universe, length, dims)


def _populate_universe(initial_state: List[List[str]], num_cycles: int,
                       length: int, dims: int) -> Dict[Tuple, str]:
  universe = _build_universe(length, dims)
  for row in range(len(initial_state)):
    for col in range(len(initial_state[row])):
      if dims == 4:
        universe[num_cycles + row, num_cycles + col, 0, 0] \
          = initial_state[row][col]
      else:
        universe[num_cycles + row, num_cycles + col, 0] \
          = initial_state[row][col]
  return universe


def _build_universe(length: int, dims: int) -> Dict[Tuple, str]:
  diameter = length // 2
  universe = {}
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        if dims == 4:
          for w in range(-diameter, diameter + 1):
            universe[x, y, z, w] = '.' # Fill with inactive cubes
        else:
          universe[x, y, z] = '.'  # Fill with inactive cubes
  return universe


def _simulate(universe: Dict[Tuple, str],
              length: int, dims: int) -> Dict[Tuple, str]:
  after = deepcopy(universe)
  diameter = length // 2
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        if dims == 4:
          for w in range(-diameter, diameter + 1):
            _simulate_point(universe, length, (x, y, z, w), after)
        else:
          _simulate_point(universe, length, (x, y, z), after)
  return after


def _simulate_point(universe: Dict[Tuple, str], length, point: Tuple,
                    after: Dict[Tuple, str]) -> None:
  num_active_neighbours = \
    _count_active_neighbours(universe, length, point)
  if universe[point] == '#' and \
      not (num_active_neighbours == 2 or num_active_neighbours == 3):
    after[point] = '.'  # converts to inactive
  elif universe[point] == '.' and num_active_neighbours == 3:
    after[point] = '#'  # converts to active


def _count_active_neighbours(universe: Dict[Tuple, str],
                             length: int, point: Tuple) -> int:
  num_active_neighbours = 0
  diameter = length // 2
  for x in range(point[0] - 1, point[0] + 2):
    for y in range(point[1] - 1, point[1] + 2):
      for z in range(point[2] - 1, point[2] + 2):
        if x < 0 or x >= length:
          continue
        if y < 0 or y >= length:
          continue
        if z < -diameter or z > diameter:
          continue
        if len(point) == 4:
          for w in range(point[3] - 1, point[3] + 2):
            if (x, y, z, w) == point:
              continue
            if w < -diameter or w > diameter:
              continue
            num_active_neighbours += 1 if universe[x, y, z, w] == '#' else 0
        else:
          if (x, y, z) == point:
            continue
          num_active_neighbours += 1 if universe[x, y, z] == '#' else 0
  return num_active_neighbours


def _count_active_cubes(universe: Dict[Tuple, str], length: int,
                        dims: int) -> int:
  num_active_cubes = 0
  diameter = length // 2
  for x in range(length):
    for y in range(length):
      for z in range(-diameter, diameter + 1):
        if dims == 4:
          for w in range(-diameter, diameter + 1):
            num_active_cubes += 1 if universe[x, y, z, w] == '#' else 0
        else:
          num_active_cubes += 1 if universe[x, y, z] == '#' else 0
  return num_active_cubes