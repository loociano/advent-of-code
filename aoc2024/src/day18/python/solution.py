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


def min_steps_to_exit(input: Sequence[str], num_bytes: int = 1024,
                      width: int = 71, length: int = 71) -> int:
  corrupted_positions = tuple(map(lambda entry: tuple(map(int, entry.split(','))), input))
  grid = [[_NOT_CORRUPTED for _ in range(width)] for _ in range(length)]
  for i in range(num_bytes):
    pos = corrupted_positions[i]
    grid[pos[1]][pos[0]] = _CORRUPTED
  return shortest_distance_bfs(grid=grid, predicate=lambda x, y: grid[y][x] != _CORRUPTED)
