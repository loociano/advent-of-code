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

type Pos = tuple[int, int]  # (y,x)


def _dfs_helper(pos: Pos, flower: str, garden_map: Sequence[str],
                visited: set[Pos], area: list[int], perimeter: list[int]):
  if (pos[0] < 0 or pos[0] > len(garden_map) - 1
          or pos[1] < 0 or pos[1] > len(garden_map[0]) - 1):
    # Out of bounds.
    perimeter[0] += 1
    visited.add(pos)
    return
  if garden_map[pos[0]][pos[1]] != flower:
    # Facing another region.
    perimeter[0] += 1
    return
  # Same region.
  area[0] += 1
  visited.add(pos)
  for direction in ((-1, 0), (0, 1), (1, 0), (0, -1)):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos not in visited:
      _dfs_helper(next_pos, flower, garden_map, visited, area, perimeter)


def calculate_fencing_price(garden_map: Sequence[str]) -> int:
  """Calculates the price to fence all regions.
  A region price is calculated as its area multiplied by its perimeter."""
  visited: dict[str, set[Pos]] = defaultdict(set)  # Tracks region positions.
  total_price = 0
  for y in range(len(garden_map)):
    for x in range(len(garden_map[0])):
      flower = garden_map[y][x]
      pos = (y, x)
      if pos not in visited[flower]:
        area, perimeter = [0], [0]  # Pass by reference
        _dfs_helper(pos, garden_map[y][x], garden_map, visited[flower], area, perimeter)
        total_price += area[0] * perimeter[0]
  return total_price
