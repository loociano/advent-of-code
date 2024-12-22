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
_TRACK = '.'
_START = 'S'
_END = 'E'


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
          and char_at(grid, enter_pos) in (_TRACK, _START, _END)
          and char_at(grid, exit_pos) in (_TRACK, _START, _END))


def _find_cheat_savings(grid: list[list[str]],
                        distance_from_start: dict[Position, int],
                        max_cheat_length: int,
                        ) -> dict[int, set[tuple[Position, Position]]]:
  """Produces a dictionary of all cheats that save time, keyed by saving time in picoseconds."""
  cheats_savings: dict[int, set[tuple[Position, Position]]] = defaultdict(set)
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] in (_TRACK, _START):
        _find_cheat_savings_from_pos(grid=grid, start_pos=(x, y),
                                     distance_from_start=distance_from_start,
                                     cheat_savings=cheats_savings,
                                     max_cheat_length=max_cheat_length)
  return cheats_savings


def _find_cheat_savings_from_pos(grid: list[list[str]],
                                 start_pos: Position,
                                 distance_from_start: dict[Position, int],
                                 cheat_savings: dict[int, set[tuple[Position, Position]]],
                                 max_cheat_length: int) -> None:
  """Finds cheats that save time from a position in the grid."""
  queue = deque()
  visited: set[Position] = set()
  queue.append((start_pos, 0))  # Queue cheat length from position.
  while queue:
    curr, cheat_length = queue.popleft()
    if curr != start_pos and char_at(grid, curr) in (_TRACK, _END):
      savings = distance_from_start[curr] - distance_from_start[start_pos] - cheat_length
      if savings > 0:
        cheat_savings[savings].add((start_pos, curr))
    for dxy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
      next_pos = (curr[0] + dxy[0], curr[1] + dxy[1])
      if (within_bounds(grid, next_pos)
              and next_pos not in visited
              and cheat_length < max_cheat_length):
        visited.add(next_pos)
        queue.append((next_pos, cheat_length + 1))


def count_cheats(racetrack: Sequence[str], min_picosec_savings: int,
                 max_cheat_length: int = 2) -> int:
  grid = [list(line) for line in racetrack]
  distance_from_start: dict[Position, int] = defaultdict(int)
  # Traverse for Start to End storing distances from Start to positions in path.
  shortest_distance_bfs(grid=grid,
                        distance_from_start=distance_from_start,
                        visited=set(),
                        start_pos=find(grid, _START),
                        end_pos=find(grid, _END),
                        predicate=lambda x, y: grid[y][x] != _WALL)
  cheat_savings = _find_cheat_savings(grid, distance_from_start, max_cheat_length)
  return sum(len(cheats) if picosec_savings >= min_picosec_savings else 0
             for picosec_savings, cheats in cheat_savings.items())
