# Copyright 2022 Google LLC
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
from typing import Sequence, TypeAlias
from collections import deque

Range: TypeAlias = tuple[int, int]


def _calc_min_max(rock_paths: Sequence[str]) -> tuple[Range, Range]:
  width = [1_000, 0]
  height = [1_000, 0]
  for path in rock_paths:
    xy_list = path.split(' -> ')
    width[0] = min(min([int(i.split(',')[0]) for i in xy_list]), width[0])
    width[1] = max(max([int(i.split(',')[0]) for i in xy_list]), width[1])
    height[0] = min(min([int(i.split(',')[1]) for i in xy_list]), height[0])
    height[1] = max(max([int(i.split(',')[1]) for i in xy_list]), height[1])
  return (width[0], width[1]), (height[0], height[1])


def _paint_paths(rock_paths: Sequence[str],
                 grid: list[list[str, ...]], min_x: int) -> None:
  for rock_path in rock_paths:
    last_x = None
    last_y = None
    xy_queue = deque(rock_path.split(' -> '))
    while len(xy_queue):
      x, y = tuple(map(int, xy_queue.popleft().split(',')))
      if last_x is None:
        last_x = x
      if last_y is None:
        last_y = y
      # Paint.
      range_x = range(last_x, x + 1) if x >= last_x else range(x, last_x + 1)
      for i in range_x:
        grid[last_y][i - min_x] = '#'  # Rock.
      range_y = range(last_y, y + 1) if y >= last_y else range(y, last_y + 1)
      for i in range_y:
        grid[i][last_x - min_x] = '#'  # Rock.
      last_x = x
      last_y = y


def _drop_sand_unit(grid: list[list[str]], min_x: int,
                    start_x: int) -> bool:
  target_x = start_x
  target_y = None
  for i in range(len(grid)):
    if target_x - min_x - 1 < 0 or target_x - min_x + 1 >= len(grid[0]):
      # Reached abysm!
      return False
    else:
      if i > 0 and grid[i][target_x - min_x] != '.':
        # Found a blocker at i.
        if grid[i][target_x - min_x - 1] == '.':  # Try left
          target_x -= 1
        elif grid[i][target_x - min_x + 1] == '.':  # Try right
          target_x += 1
        else:
          target_y = i - 1
          break
  if target_y is None:
    return False
  grid[target_y][target_x - min_x] = 'o'  # Rest at target.
  return True


def _build_grid(rock_paths: Sequence[str]) -> tuple[list[list[str]], int]:
  x_range, y_range = _calc_min_max(rock_paths)
  width = x_range[1] - x_range[0] + 1
  grid = []
  for _ in range(y_range[1] + 1):
    grid.append(['.'] * width)
  _paint_paths(rock_paths=rock_paths, grid=grid, min_x=x_range[0])
  return grid, x_range[0]


def _count_sand_units(grid: list[list[str]]) -> int:
  return sum([line.count('o') for line in grid])


def count_resting_sand_units(rock_paths: Sequence[str]) -> int:
  rested = True
  grid, min_x = _build_grid(rock_paths)
  # Drop units of sand until one does not rest (reaches abysm).
  while rested:
    rested = _drop_sand_unit(grid=grid, min_x=min_x, start_x=500)
  return _count_sand_units(grid)
