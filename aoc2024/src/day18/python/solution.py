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
from collections import defaultdict, deque

_CORRUPTED = '#'
_NOT_CORRUPTED = '.'

type Position = tuple[int, int]  # (x,y)


def shortest_path_bfs(grid: list[list[str]], visited: set[Position], start_pos: Position = (0, 0),
                      end_pos: Position = None):
  if end_pos is None:
    end_pos = (len(grid[0]) - 1, len(grid) - 1)  # (x,y)
  queue = deque()
  queue.append((start_pos, 0))  # level
  while queue:
    pos, level = queue.popleft()
    if pos == end_pos:
      return level
    for dxy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
      next_pos = (pos[0] + dxy[0], pos[1] + dxy[1])
      if (next_pos not in visited
              and 0 <= next_pos[0] < len(grid[0])
              and 0 <= next_pos[1] < len(grid)
              and grid[next_pos[1]][next_pos[0]] != _CORRUPTED):
        visited.add(next_pos)
        queue.append((next_pos, level + 1))


def min_steps_to_exit(input: Sequence[str], num_bytes: int = 1024,
                      width: int = 71, length: int = 71) -> int:
  corrupted_positions = tuple(map(lambda entry: tuple(map(int, entry.split(','))), input))
  grid = [[_NOT_CORRUPTED for _ in range(width)] for _ in range(length)]
  for i in range(num_bytes):
    pos = corrupted_positions[i]
    grid[pos[1]][pos[0]] = _CORRUPTED
  return shortest_path_bfs(grid=grid, visited=set())
