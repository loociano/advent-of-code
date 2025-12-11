# Copyright 2025 Google LLC
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
from common.python3.graph_utils import char_at, within_bounds
from common.python3.types import Position

_PAPER_ROLL = '@'


def _is_roll(grid: Sequence[Sequence[str]], pos: Position) -> bool:
  """Returns True if there is a roll of paper at the given position."""
  return char_at(grid=grid, pos=pos) == _PAPER_ROLL


def _can_access_roll(grid: Sequence[Sequence[str]], pos: Position) -> bool:
  """Returns True if forklifts can access a roll at a given position.

  Forklifts can only access a roll of paper if there are fewer than four rolls
  of paper in the eight adjacent positions.
  """
  adj_rolls = 0
  for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]:
      if dx == 0 and dy == 0:
        continue  # Skip original position.
      adj_pos = (pos[0] + dy, pos[1] + dx)
      if not within_bounds(grid=grid, pos=adj_pos):
        continue  # Skip out of bounds.
      if char_at(grid=grid, pos=adj_pos) == _PAPER_ROLL:
        adj_rolls += 1
        if adj_rolls == 4:
          return False
  return True


def _is_accessible_roll(grid: Sequence[Sequence[str]], pos: Position) -> bool:
  return _is_roll(grid=grid, pos=pos) and _can_access_roll(grid=grid, pos=pos)


def count_accessible_rolls(grid: Sequence[Sequence[str]]) -> int:
  return sum(1
             for y in range(len(grid))
             for x in range(len(grid[0]))
             if _is_accessible_roll(grid=grid, pos=(y, x)))


def remove_rolls(grid: Sequence[Sequence[str]]) -> int:
  """Iteratively removes accessible rolls and returns total removed."""
  removed = 0
  mutable_grid = list(list(row) for row in grid)
  while count_accessible_rolls(grid=mutable_grid) != 0:
    to_be_removed: list[Position] = []
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        if _is_accessible_roll(grid=mutable_grid, pos=(y, x)):
          to_be_removed.append((y, x))
    for pos in to_be_removed:
      mutable_grid[pos[1]][pos[0]] = '.'
    removed += len(to_be_removed)
  return removed
