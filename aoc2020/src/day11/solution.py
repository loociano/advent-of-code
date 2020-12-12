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
from typing import List, Callable
from copy import deepcopy


def part_one(grid: List[List[str]]) -> int:
  """
  Returns:
    Number of occupied seats.
  """
  return _simulate_until_stable(grid,
                                lambda g, r, c: _count_adj_occupied(g, r, c))


def part_two(grid: List[List[str]]) -> int:
  """
    Returns:
      Number of occupied seats.
    """
  return _simulate_until_stable(grid,
                                lambda g, r, c: _count_seen_occupied(g, r, c),
                                min_occupied_to_free=5)


def _simulate_until_stable(
    grid: List[List[str]],
    count_occupied: Callable[[List[List[str]], int, int], int],
    min_occupied_to_free=4) -> int:
  """
  Simulates the free/occupied rules in a grid until it reaches equilibrium.
  """
  while True:
    next_grid = _simulate(grid, count_occupied, min_occupied_to_free)
    if _are_equal(next_grid, grid):
      return _count_occupied_seats(grid)
    grid = next_grid


def _print_grid(grid: List[List[str]]) -> None:
  print('')
  for row in grid:
    print(''.join(row))
  print('')

def _are_equal(grid: List[List[str]], other: List[List[str]]) -> bool:
  """
  Returns true if two grids are identical.
  """
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] != other[row][col]:
        return False
  return True


def _count_occupied_seats(grid: List[List[str]]) -> int:
  """
  Counts the total number of occupied seats in a grid.
  """
  total = 0
  for row in grid:
    total += row.count('#')
  return total


def _simulate(
    grid: List[List[str]],
    count_occupied: Callable[[List[List[str]], int, int], int],
    min_occupied_to_free: int
) -> List[List[str]]:
  """
  Returns:
    The next state of the grid.
  """
  next_grid = deepcopy(grid)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      next_grid[row][col] = \
        _simulate_seat(grid, row, col, count_occupied, min_occupied_to_free)
  return next_grid


def _simulate_seat(
    grid: List[List[str]],
    row: int,
    col: int,
    count_occupied: Callable[[List[List[str]], int, int], int],
    min_occupied_to_free: int) -> str:
  """
  Simulates the occupy/free rules to a given position in the grid.
  """
  seat = grid[row][col]
  if seat == 'L' and count_occupied(grid, row, col) == 0:
    return '#'  # occupied
  if seat == '#' and count_occupied(grid, row, col) >= min_occupied_to_free:
    return 'L'
  return seat


def _count_adj_occupied(grid: List[List[str]], row: int, col: int) -> int:
  """
  Counts the number of adjacent occupied seats, including diagonals.
  """
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


def _count_seen_occupied(grid: List[List[str]], row: int, col: int) -> int:
  """
  Counts the number of occupied seats that can be seen from a position in grid.
  """
  count = 0
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if not (dx == 0 and dy == 0):
        count += 1 if _is_occupied(grid, row, col, dx, dy) else 0
  return count


def _is_occupied(
    grid: List[List[str]], row: int, col: int, dx: int, dy: int) -> bool:
  """
  Returns True if an occupied seat can be seen from a position in the grid
   and a direction (dx, dy). Empty seats block the view.
  """
  while 0 <= (row + dy) < len(grid) and 0 <= (col + dx) < len(grid[0]):
    row += dy
    col += dx
    if grid[row][col] == 'L':
      return False
    if grid[row][col] == '#':
      return True
  return False