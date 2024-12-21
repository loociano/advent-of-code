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
from common.python3.graph_utils import shortest_distance_bfs

_CORRUPTED = '#'
_NOT_CORRUPTED = '.'


def _corrupt_grid(grid: list[list[str]], corrupted_positions: tuple[tuple[int, ...], ...]) -> None:
  for i in range(len(corrupted_positions)):
    pos = corrupted_positions[i]
    grid[pos[1]][pos[0]] = _CORRUPTED


def min_steps_to_exit(input: Sequence[str], num_bytes: int = 1024,
                      width: int = 71, length: int = 71) -> int:
  corrupted_positions = tuple(map(lambda entry: tuple(map(int, entry.split(','))), input))
  grid = [[_NOT_CORRUPTED for _ in range(width)] for _ in range(length)]
  _corrupt_grid(grid, corrupted_positions[:num_bytes])
  return shortest_distance_bfs(grid=grid, predicate=lambda x, y: grid[y][x] != _CORRUPTED)


def find_first_byte_preventing_exit(input: Sequence[str],
                                    width: int = 71, length: int = 71) -> int:
  corrupted_positions = tuple(map(lambda entry: tuple(map(int, entry.split(','))), input))
  for i in range(len(corrupted_positions)):
    try:
      grid = [[_NOT_CORRUPTED for _ in range(width)] for _ in range(length)]
      _corrupt_grid(grid, corrupted_positions[:i + 1])
      _ = shortest_distance_bfs(grid=grid, predicate=lambda x, y: grid[y][x] != _CORRUPTED)
    except ValueError:
      # Found the byte that prevents the exit.
      return corrupted_positions[i]
  raise ValueError('There is no byte that prevents the exit.')
