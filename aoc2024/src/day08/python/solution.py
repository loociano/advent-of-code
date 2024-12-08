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
from typing import Sequence
from collections import defaultdict

_NO_ANTENNA = '.'

# Antenas
type Pos = tuple[int, int]


def _find_antennas(city_map: Sequence[str]) -> dict[str, set[Pos]]:
  """Finds antenna locations and groups them by frequency.
  Frequency is represented by character, for example 'a'."""
  antennas = defaultdict(set)
  for y in range(len(city_map)):
    for x in range(len(city_map[0])):
      value = city_map[y][x]
      if value != _NO_ANTENNA:
        antennas[value].add((y, x))
  return antennas


def _within_bounds(pos: Pos, bounds: Pos) -> bool:
  """Returns true if a position is within city bounds."""
  return 0 <= pos[0] < bounds[0] and 0 <= pos[1] < bounds[1]


def count_antinodes(city_map: Sequence[str], any_grid_position=False) -> int:
  """Counts the antinodes resulting from antennas in the city."""
  city_bounds = (len(city_map[0]), len(city_map))
  antennas: dict[chr, set[Pos]] = _find_antennas(city_map)
  antinode_positions: set[Pos] = set()
  for positions in antennas.values():
    for curr_pos in positions:
      for other_pos in positions:
        if curr_pos == other_pos:
          continue  # Skip same antenna.
        distance = (other_pos[0] - curr_pos[0], other_pos[1] - curr_pos[1])
        if any_grid_position:
          next_pos = (curr_pos[0] + distance[0], curr_pos[1] + distance[1])
          while _within_bounds(next_pos, city_bounds):
            antinode_positions.add(next_pos)
            next_pos = (next_pos[0] + distance[0], next_pos[1] + distance[1])
        else:
          antinode_pos = (other_pos[0] + distance[0], other_pos[1] + distance[1])
          if _within_bounds(pos=antinode_pos, bounds=city_bounds):
            antinode_positions.add(antinode_pos)
  return len(antinode_positions)
