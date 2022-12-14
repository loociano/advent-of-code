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
from collections import defaultdict, deque
from typing import Dict, List, Tuple, TypeAlias

Coord: TypeAlias = Tuple[int, int]
Graph: TypeAlias = Dict[Coord, List[Coord]]


def _build_graph(grid: Tuple[Tuple[str, ...]]) -> Tuple[Graph, Coord, Coord]:
  graph = defaultdict(list)
  start = None
  end = None
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      point = (row, col)
      value = grid[row][col]
      if value == 'S':
        start = point
        height = ord('a')
      elif value == 'E':
        end = point
        height = ord('z')
      else:
        height = ord(value)
      neighbours = (
        (row - 1, col),  # Up
        (row, col + 1),  # Right
        (row + 1, col),  # Down
        (row, col - 1),  # Left
      )
      for neighbour_row, neighbour_col in neighbours:
        if (neighbour_row < 0
            or neighbour_row >= len(grid)
            or neighbour_col < 0
            or neighbour_col >= len(grid[0])):
          continue
        neighbour_value = grid[neighbour_row][neighbour_col]
        if neighbour_value == 'S':
          neighbour_height = ord('a')
        elif neighbour_value == 'E':
          neighbour_height = ord('z')
        else:
          neighbour_height = ord(neighbour_value)
        if neighbour_height - height <= 1:
          graph[point].append((neighbour_row, neighbour_col))
  return graph, start, end


def _bfs(graph: Graph, start: Coord, end: Coord) -> int:
  shortest_path_seen = {start: 0}
  queue = deque()
  queue.append((start, 0))
  while len(queue):
    current_position, steps = queue.popleft()
    current_steps = steps + 1
    for neighbour in graph[current_position]:
      if (
          neighbour not in shortest_path_seen
          or current_steps < shortest_path_seen[neighbour]
      ):
        shortest_path_seen[neighbour] = current_steps
        if neighbour != end:
          queue.append((neighbour, current_steps))
  if shortest_path_seen.get(end) is None:
    # Top cannot be reached from every point.
    return 100_000_000
  return shortest_path_seen[end]


def _find_coords(grid: Tuple[Tuple[str, ...]],
                 search: str = 'a') -> List[Coord]:
  result = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == search:
        result.append((row, col))
  return result


def min_steps_to_top(heightmap: Tuple[Tuple[str, ...]],
                     start_char: str = 'S') -> int:
  grid = tuple([tuple(list(line)) for line in heightmap])
  graph, start, end = _build_graph(grid)
  if start_char != 'S':
    starting_coords = _find_coords(grid=grid, search=start_char) + [start]
    return min([_bfs(graph=graph, start=start_coord, end=end)
                for start_coord in starting_coords])
  return _bfs(graph=graph, start=start, end=end)
