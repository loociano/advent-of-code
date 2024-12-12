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


def _update_perimeter(perimeters: dict[str, list[int]], pos: Pos, direction: tuple[int, int]):
  """Updates perimeter data."""
  if direction in ((0, 1), (0, -1)):  # Left/right
    perimeters[f'{direction}:{pos[1]}'].append(pos[0])
  else:  # Up/down
    perimeters[f'{direction}:{pos[0]}'].append(pos[1])


def _dfs_helper(pos: Pos, flower: str, garden_map: Sequence[str],
                visited: set[Pos], area: list[int], perimeters: dict[str, list[int]],
                direction: tuple[int, int] | None = None):
  """Traverses the garden with DSF, tracking area and perimeter data."""
  if (pos[0] < 0 or pos[0] > len(garden_map) - 1
          or pos[1] < 0 or pos[1] > len(garden_map[0]) - 1):
    # Out of bounds.
    _update_perimeter(perimeters, pos, direction)
    visited.add(pos)
    return
  if garden_map[pos[0]][pos[1]] != flower:
    # Facing another region.
    _update_perimeter(perimeters, pos, direction)
    return
  # Same region.
  area[0] += 1
  visited.add(pos)
  for direction in ((-1, 0), (0, 1), (1, 0), (0, -1)):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos not in visited:
      _dfs_helper(next_pos, flower, garden_map, visited, area, perimeters, direction)


def _calculate_sides(perimeters: dict[str, list[int]]) -> int:
  """Calculates number of sides given perimeter data."""
  sides = 0
  for coords in perimeters.values():
    sides += 1  # Each group of coordinates represents at least one side.
    sorted_coords = sorted(coords)
    for i in range(1, len(sorted_coords)):
      if sorted_coords[i] > sorted_coords[i - 1] + 1:
        # Coordinates are disjointed, hence 2 different sides.
        sides += 1
  return sides


def calculate_fencing_price(garden_map: Sequence[str], price_by_side=False) -> int:
  """Calculates the price to fence all regions.
  A region price is calculated as its area multiplied by its perimeter."""
  visited: dict[str, set[Pos]] = defaultdict(set)  # Tracks region positions.
  total_price = 0
  for y in range(len(garden_map)):
    for x in range(len(garden_map[0])):
      flower = garden_map[y][x]
      pos = (y, x)
      if pos not in visited[flower]:
        area = [0]  # Pass by reference
        # Track perimeter data. Key by direction at x or y coordinate:
        # UP/DOWN at x coordinate -> list of y coordinates
        # LEFT/RIGHT at y coordinate -> list of x coordinates
        perimeters: dict[str, list[int]] = defaultdict(list)
        _dfs_helper(pos, garden_map[y][x], garden_map, visited[flower], area, perimeters)
        if price_by_side:
          total_price += area[0] * _calculate_sides(perimeters)
        else:
          total_price += area[0] * sum([len(values) for values in perimeters.values()])
  return total_price
