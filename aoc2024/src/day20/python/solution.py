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
from collections import defaultdict, deque
from typing import Any, Callable, Sequence
from common.python3.graph_utils import find, within_bounds, char_at
from common.python3.types import Direction, Position

_WALL = '#'
_SPACE = '.'
_START = 'S'
_END = 'E'
_CHEAT_COST = 2


def shortest_distance_bfs(grid: list[list[str]], distance_from_start: dict[Position, int] = None,
                          visited: set[Position] = None,
                          start_pos: Position = (0, 0), end_pos: Position = None,
                          directions: tuple[Direction, ...] = ((0, -1), (1, 0), (0, 1), (-1, 0)),
                          predicate: Callable[[Any, ...], bool] = None) -> None:
  """Populates distances from every position in the shortest path to the start position."""
  queue = deque()
  queue.append((start_pos, 0))  # Append level.
  while queue:
    pos, level = queue.popleft()
    visited.add(pos)
    distance_from_start[pos] = level
    if pos == end_pos:
      return
    for dxy in directions:
      next_pos = (pos[0] + dxy[0], pos[1] + dxy[1])
      if (next_pos not in visited
              and 0 <= next_pos[0] < len(grid[0])
              and 0 <= next_pos[1] < len(grid)
              and predicate(next_pos[0], next_pos[1])):
        queue.append((next_pos, level + 1))
  raise ValueError('Could not reach the exit.')


def _is_valid_cheat_path(grid: list[list[str]], enter_pos: Position, exit_pos: Position) -> bool:
  """Returns true if 2 positions in the grid constitute a valid passage cheat."""
  return (within_bounds(grid, enter_pos)
          and within_bounds(grid, exit_pos)
          and char_at(grid, enter_pos) in (_SPACE, _START, _END)
          and char_at(grid, exit_pos) in (_SPACE, _START, _END))


def _find_cheat_savings(grid: list[list[str]], distance_from_start: dict[Position, int]) -> dict[int, int]:
  cheats_savings = defaultdict(int)
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == _WALL:
        vertical = ((x, y - 1), (x, y + 1))
        if _is_valid_cheat_path(grid, enter_pos=vertical[0], exit_pos=vertical[1]):
          savings = abs(distance_from_start[vertical[0]] - distance_from_start[vertical[1]]) - _CHEAT_COST
          cheats_savings[savings] += 1
        horizontal = ((x - 1, y), (x + 1, y))
        if _is_valid_cheat_path(grid, enter_pos=horizontal[0], exit_pos=horizontal[1]):
          savings = abs(
            distance_from_start[horizontal[0]] - distance_from_start[horizontal[1]]) - _CHEAT_COST
          cheats_savings[savings] += 1
  return cheats_savings


def count_cheats(racetrack: Sequence[str], min_picosec_savings: int) -> int:
  grid = [list(line) for line in racetrack]
  distance_from_start: dict[Position, int] = defaultdict(int)
  # Traverse for Start to End storing distances from Start to positions in path.
  shortest_distance_bfs(grid=grid,
                        distance_from_start=distance_from_start,
                        visited=set(),
                        start_pos=find(grid, _START),
                        end_pos=find(grid, _END),
                        predicate=lambda x, y: grid[y][x] != _WALL)
  cheat_savings = _find_cheat_savings(grid, distance_from_start)
  return sum(frequency if picosec_savings >= min_picosec_savings else 0
             for picosec_savings, frequency in cheat_savings.items())
