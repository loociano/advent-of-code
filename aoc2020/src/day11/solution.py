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
from typing import List
from copy import deepcopy


def part_one(grid: List[List[str]]) -> int:
  """
  Returns:
    Number of occupied seats.
  """
  while True:
    next_grid = _simulate(grid)
    if _are_equal(next_grid, grid):
      return _count_occupied_seats(grid)
    grid = next_grid


def _print_grid(grid: List[List[str]]) -> None:
  print('')
  for row in grid:
    print(''.join(row))
  print('')

def _are_equal(grid: List[List[str]], other: List[List[str]]) -> bool:
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] != other[row][col]:
        return False
  return True


def _count_occupied_seats(grid: List[List[str]]) -> int:
  total = 0
  for row in grid:
    total += row.count('#')
  return total


def _simulate(grid: List[List[str]]) -> List[List[str]]:
  """
  Returns:
    The next state of the grid.
  """
  next_grid = deepcopy(grid)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      next_grid[row][col] = _simulate_seat(grid, row, col, )
  return next_grid


def _simulate_seat(grid: List[List[str]], row: int, col: int) -> str:
  seat = grid[row][col]
  if seat == 'L' and _count_adj_occupied(grid, row, col) == 0:
    return '#'  # occupied
  if seat == '#' and _count_adj_occupied(grid, row, col) >= 4:
    return 'L'
  return seat


def _count_adj_occupied(grid: List[List[str]], row: int, col: int) -> int:
  count = 0
  if row - 1 >= 0:
    if col - 1 >= 0:
      count += 1 if grid[row - 1][col - 1] == '#' else 0
    if col + 1 < len(grid[0]):
      count += 1 if grid[row - 1][col + 1] == '#' else 0
    count += 1 if grid[row - 1][col] == '#' else 0
  if row + 1 < len(grid):
    if col - 1 >= 0:
      count += 1 if grid[row + 1][col - 1] == '#' else 0
    if col + 1 < len(grid[0]):
      count += 1 if grid[row + 1][col + 1] == '#' else 0
    count += 1 if grid[row + 1][col] == '#' else 0
  if col - 1 >= 0:
    count += 1 if grid[row][col - 1] == '#' else 0
  if col + 1 < len(grid[0]):
    count += 1 if grid[row][col + 1] == '#' else 0
  return count


def part_two(grid: List[List[str]]) -> int:
  """
    Returns:
      Number of occupied seats.
    """
  return -1